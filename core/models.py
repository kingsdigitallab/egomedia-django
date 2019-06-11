from core.blocks import HomePageStreamBlock, TimelineStreamBlock
from django import forms
from django.db import models
from kdl_wagtail.core.models import (
    BasePage, BaseStreamPage, IndexPage, RichTextPage, StreamPage
)
from kdl_wagtail.people.models import (
    PeopleIndexPage, Person, PersonModel, PersonPage
)
from kdl_wagtail.zotero.models import Bibliography, BibliographyIndexPage
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, PageChooserPanel,
    StreamFieldPanel
)
from wagtail.api import APIField
from wagtail.core.fields import RichTextField, StreamField
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

    def get_facets(self):
        return [
            ('discipline', self.disciplines.values_list('title', flat=True)),
            ('focus', self.focus.values_list('title', flat=True)),
            ('keyword', self.keywords.values_list('title', flat=True)),
            ('method', self.methods.values_list('title', flat=True)),
        ]

    def get_page_facets(self):
        pass


class EndNoteMixin(ClusterableModel):
    pre_text = RichTextField(blank=True, null=True)
    bibliography_entry = models.ForeignKey(
        Bibliography, blank=True, null=True, on_delete=models.SET_NULL)
    bibliography_pages = models.CharField(
        max_length=256, blank=True, null=True)
    bibliography_shortnote = models.BooleanField()
    post_text = RichTextField(blank=True, null=True)

    panels = [
        FieldPanel('pre_text'),
        SnippetChooserPanel('bibliography_entry', Bibliography),
        FieldPanel('bibliography_pages'),
        FieldPanel('bibliography_shortnote'),
        FieldPanel('post_text')
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

    subpage_types = [BibliographyIndexPage,
                     IndexPage, PeopleIndexPage, StreamPage]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        filters = [
            ('theme',
             ThemePage.objects.live().order_by(
                 'title').values_list('title', flat=True)),
            ('researcher',
             ResearcherPage.objects.live().order_by(
                 'title').values_list('title', flat=True)),
            ('project',
             ProjectPage.objects.live().order_by(
                 'title').values_list('title', flat=True)),
            ('discipline', Discipline.objects.values_list('title', flat=True)),
            ('focus', Focus.objects.values_list('title', flat=True)),
            ('method', Method.objects.values_list('title', flat=True)),
            ('keyword', Keyword.objects.values_list('title', flat=True))
        ]

        context['filters'] = filters

        descendants = Page.objects.live().descendant_of(self)
        pages = descendants.type(ThemePage) | descendants.type(
            ResearcherPage) | descendants.type(ProjectPage)

        context['pages'] = pages

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

    def get_page_facets(self):
        related = self.researcher_project_relationship.all()
        projects = ProjectPage.objects.live().filter(
            project_researcher_relationship__in=related)

        related = self.researcher_theme_relationship.all()
        themes = ThemePage.objects.live().filter(
            theme_researcher_relationship__in=related)

        secondary_themes = ThemePage.objects.none()

        for p in projects:
            secondary_themes = secondary_themes | p.get_themes()

        secondary_themes = secondary_themes.distinct()
        secondary_themes = secondary_themes.difference(themes)

        return [
            ('theme', themes),
            ('theme', secondary_themes),
            ('project', projects)
        ]


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
        index.SearchField('body'),
    ]

    class Meta:
        abstract = True

    def get_endnotes_by_entry(self):
        return self.endnotes.order_by('bibliography_entry__order')


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
        InlinePanel('endnotes', label='EndNotes'),
        InlinePanel('project_theme_relationship',
                    label='Themes', panels=None, min_num=1),
        InlinePanel('project_researcher_relationship',
                    label='Researchers', panels=None, min_num=1),
    ] + FacetsMixin.content_panels

    parent_page_types = [IndexPage, 'ProjectPage']
    subpage_types = ['ProjectPage']

    def get_page_facets(self):
        related = self.project_researcher_relationship.all()
        researchers = ResearcherPage.objects.live().filter(
            researcher_project_relationship__in=related)

        return [
            ('theme', self.get_themes()),
            ('researcher', researchers)
        ]

    def get_themes(self):
        related = self.project_theme_relationship.all()
        return ThemePage.objects.live().filter(
            theme_project_relationship__in=related)


class ProjectEndnote(Orderable, EndNoteMixin):
    project = ParentalKey(
        ProjectPage, on_delete=models.CASCADE, related_name='endnotes')


class ThemePage(BaseTimelinePage, FacetsMixin):
    content_panels = BaseTimelinePage.content_panels + [
        InlinePanel('endnotes', label='EndNotes')
    ] + FacetsMixin.content_panels

    parent_page_types = [IndexPage]
    subpage_types = []

    def get_page_facets(self):
        related = self.theme_project_relationship.all()
        projects = ProjectPage.objects.live().filter(
            project_theme_relationship__in=related)

        related = self.theme_researcher_relationship.all()
        researchers = ResearcherPage.objects.live().filter(
            researcher_theme_relationship__in=related)

        return [
            ('researcher', researchers),
            ('project', projects)
        ]


class ThemeEndnote(Orderable, EndNoteMixin):
    theme = ParentalKey(
        ThemePage, on_delete=models.CASCADE, related_name='endnotes')


# Sets up pages' visibility
BibliographyIndexPage.parent_page_types = [HomePage]
BibliographyIndexPage.subpage_types = []

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
