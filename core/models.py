from core.blocks import HomePageStreamBlock, TimelineStreamBlock
from django import forms
from django.db import models
from kdl_wagtail.core.models import (BasePage, BaseStreamPage, IndexPage,
                                     RichTextPage, StreamPage)
from kdl_wagtail.people.models import (PeopleIndexPage, Person, PersonModel,
                                       PersonPage)
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.api import APIField
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

# hides the generic image field
BasePage.content_panels.pop(2)
BasePage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('image')
]


class BaseFacet(index.Indexed, ClusterableModel):
    title = models.CharField(max_length=64, unique=True)

    api_fields = [
        APIField('_title')
    ]

    panels = [
        FieldPanel('title', 'full')
    ]

    search_fields = [
        index.SearchField('title')
    ]

    class Meta:
        abstract = True
        ordering = ['title']

    def __str__(self):
        return self.title


@register_snippet
class Discipline(BaseFacet):
    pass


@register_snippet
class Focus(BaseFacet):
    class Meta(BaseFacet.Meta):
        verbose_name_plural = 'Focus'


@register_snippet
class Keyword(BaseFacet):
    pass


@register_snippet
class Method(BaseFacet):
    pass


class FacetsMixin(models.Model):
    disciplines = ParentalManyToManyField(Discipline, blank=True)
    focus = ParentalManyToManyField(Focus, blank=True)
    keywords = ParentalManyToManyField(Keyword, blank=True)
    methods = ParentalManyToManyField(Method, blank=True)

    content_panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel(
                    'disciplines', classname='col6',
                    widget=forms.CheckboxSelectMultiple
                ),
                FieldPanel(
                    'methods', classname='col6',
                    widget=forms.CheckboxSelectMultiple
                )
            ]),
            FieldRowPanel([
                FieldPanel(
                    'focus', classname='col6',
                    widget=forms.CheckboxSelectMultiple
                ),
                FieldPanel(
                    'keywords', classname='col6',
                    widget=forms.CheckboxSelectMultiple
                )
            ])
        ], 'Facets', classname='collapsible collapsed')
    ]

    class Meta:
        abstract = True


class HomePage(Page):
    body = StreamField(HomePageStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    subpage_types = [IndexPage, PeopleIndexPage, StreamPage]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        filters = [
            ('theme', ThemePage.objects.values_list('title', flat=True)),
            ('keyword', Keyword.objects.all()),
        ]

        context['filters'] = filters

        return context


class ResearcherThemeRelationship(Orderable, models.Model):
    researcher = ParentalKey(
        'ResearcherPage', related_name='researcher_theme_relationship',
        on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'ThemePage', related_name='theme_researcher_relationship',
        on_delete=models.CASCADE
    )

    panels = [
        PageChooserPanel('theme')
    ]


class ResearcherPage(BaseStreamPage, FacetsMixin):
    person = models.ForeignKey(
        PersonModel, related_name='researcher_pages', on_delete=models.PROTECT)

    api_fields = BaseStreamPage.api_fields + [
        APIField('person')
    ]

    content_panels = [
        FieldPanel('title', classname='full'),
        SnippetChooserPanel('person'),
        StreamFieldPanel('body'),
        InlinePanel('researcher_theme_relationship',
                    label='Themes', panels=None, min_num=1)
    ] + FacetsMixin.content_panels

    search_fields = BaseStreamPage.search_fields + [
        index.RelatedFields('person', Person.search_fields)
    ]

    parent_page_types = [PeopleIndexPage]
    subpage_types = []


class BaseTimelinePage(BasePage):
    body = StreamField(TimelineStreamBlock(),
                       verbose_name='Page body', blank=True)

    api_fields = BasePage.api_fields + [
        APIField('body')
    ]

    content_panels = BasePage.content_panels + [
        StreamFieldPanel('body')
    ]

    search_fields = BasePage.search_fields + [
        index.SearchField('body')
    ]

    class Meta:
        abstract = True


class ProjectThemeRelationship(Orderable, models.Model):
    project = ParentalKey(
        'ProjectPage', related_name='project_theme_relationship',
        on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'ThemePage', related_name='theme_project_relationship',
        on_delete=models.CASCADE
    )

    panels = [
        PageChooserPanel('theme')
    ]


class ProjectResearcherRelationship(Orderable, models.Model):
    project = ParentalKey(
        'ProjectPage', related_name='project_researcher_relationship',
        on_delete=models.CASCADE
    )
    researcher = models.ForeignKey(
        'ResearcherPage', related_name='researcher_project_relationship',
        on_delete=models.CASCADE
    )

    panels = [
        PageChooserPanel('researcher')
    ]


class ProjectPage(BaseTimelinePage, FacetsMixin):
    content_panels = BaseTimelinePage.content_panels + [
        InlinePanel('project_theme_relationship',
                    label='Themes', panels=None, min_num=1),
        InlinePanel('project_researcher_relationship',
                    label='Researchers', panels=None, min_num=1),
    ] + FacetsMixin.content_panels

    parent_page_types = [IndexPage, 'ProjectPage']
    subpage_types = ['ProjectPage']


class ThemePage(BaseTimelinePage, FacetsMixin):
    content_panels = BaseTimelinePage.content_panels + \
        FacetsMixin.content_panels

    parent_page_types = [IndexPage]
    subpage_types = []


# Sets up pages' visibility
IndexPage.parent_page_types = [HomePage, IndexPage]
IndexPage.subpage_types = [IndexPage, ProjectPage, StreamPage, ThemePage]

PeopleIndexPage.parent_page_types = [HomePage]
PeopleIndexPage.subpage_types = [ResearcherPage]
PeopleIndexPage.content_panels.pop(2)

PersonPage.parent_page_types = []
PersonPage.subpage_types = []

ProjectPage.subpage_types = [ProjectPage]

RichTextPage.parent_page_types = []
RichTextPage.subpage_types = []

StreamPage.parent_page_types = [HomePage, IndexPage]

# Re-label the stream page to match the name required by this project
StreamPage._meta.verbose_name = 'Generic page'
StreamPage._meta.verbose_name_plural = 'Generic pages'
StreamPage.content_panels.pop(2)
