import json
import re
from itertools import chain

from core.blocks import HomePageStreamBlock, TimelineStreamBlock
from django import forms
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from kdl_wagtail.core.models import (
    BasePage, BaseStreamPage, IndexPage, RichTextPage, SitemapPage, StreamPage
)
from kdl_wagtail.people.models import (
    PeopleIndexPage, Person, PersonModel, PersonPage
)
from kdl_wagtail.zotero.models import Bibliography, BibliographyIndexPage
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel
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


class FacetTypeManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


@register_snippet
class FacetType(models.Model):
    title = models.CharField(max_length=64, unique=True)

    objects = FacetTypeManager()

    class Meta:
        ordering = ['title']

    def __lt__(self, other):
        return self.title < other.title

    def __gt__(self, other):
        return self.title > other.title

    def __str__(self):
        return self.title

    def natural_key(self):
        return (self.title,)


class FacetManager(models.Manager):
    def get_by_natural_key(self, facet_type, title):
        return self.get(facet_type__title=facet_type, title=title)


@register_snippet
class Facet(index.Indexed, ClusterableModel):
    facet_type = models.ForeignKey(
        FacetType, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)

    api_fields = [
        APIField('facet_type'),
        APIField('title')
    ]

    panels = [
        FieldPanel('facet_type'),
        FieldPanel('title', 'full')
    ]

    search_fields = [
        index.RelatedFields('facet_type', [
            index.SearchField('title')
        ]),
        index.SearchField('title')
    ]

    objects = FacetManager()

    class Meta:
        ordering = ['title']
        unique_together = [['facet_type', 'title']]

    def __str__(self):
        return '{}: {}'.format(self.facet_type, self.title)

    def natural_key(self):
        return self.facet_type.natural_key() + (self.title,)


class FacetsMixin(models.Model):
    facets = ParentalManyToManyField(Facet, blank=True)

    content_panels = [
        FieldPanel(
            'facets',
            classname='facets',
            widget=forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'facet-checkbox'
                }
            )
        )
    ]

    class Meta:
        abstract = True

    def get_facets(self):
        return [(f.facet_type.title, f.title) for f in self.facets.all()]

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


class TextSearchPage(BasePage):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['data'] = {}
        context['build'] = 0

        if settings.LUNR_BUILD_INDEX:
            context['build'] = 1

        context['data'] = self.get_search_data()

        return context

    @staticmethod
    def get_search_data():
        live_pages = Page.objects.live().specific()

        data = []
        sf = index.SearchField('body')

        for p in live_pages:
            content = sf.get_value(p)
            if isinstance(content, list):
                content = ' '.join(content)

            if isinstance(p, BibliographyIndexPage):
                content = '{} {}'.format(
                    content if content else '', ' '.join(
                        [e.entry for e in p.entries()])
                )

            endnotes = getattr(p, 'endnotes', None)
            if endnotes:
                for e in endnotes.all():
                    content = '{} {}; {}; {}'.format(
                        content, e.pre_text, e.bibliography_entry, e.post_text)

            if not content:
                content = ''

            content = re.sub('<[^>]*>', '', content)
            content = re.sub(r'\[\^[^\]]\]', '', content)

            data.append({
                'id': str(p.id),
                'title': p.title,
                'url': p.url,
                'content': content
            })

        return json.dumps(data)


class HomePage(Page):
    body = StreamField(HomePageStreamBlock())

    api_fields = [
        APIField('body')
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    subpage_types = [BibliographyIndexPage, IndexPage,
                     PeopleIndexPage, SitemapPage, StreamPage, TextSearchPage]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        filters = [
            ('theme',
             ThemePage.objects.live().order_by(
                 'title').values_list('title', flat=True)),
            ('researcher',
             ResearcherPage.objects.live().order_by(
                 'person__name').values_list('title', flat=True)),
            ('project',
             ProjectPage.objects.live().order_by(
                 'full_title').values_list('title', 'full_title', 'depth'))
        ]

        for ft in FacetType.objects.all():
            filters.append((
                ft.title,
                Facet.objects.filter(
                    facet_type=ft).values_list('title', flat=True)
            ))

        context['filters'] = filters

        context['pages'] = list(chain(
            ThemePage.objects.live().order_by('title'),
            ProjectPage.objects.live().order_by('title'),
            ResearcherPage.objects.live().order_by('person__name')
        ))

        context['viz_data'] = self.get_viz_data()

        return context

    @staticmethod
    def get_viz_data():
        data = []

        for p in ProjectPage.objects.live().filter(depth=4):
            data.append(p.get_viz_data())

        for r in ResearcherPage.objects.live():
            data.append(r.get_viz_data())

        for t in ThemePage.objects.live():
            data.append(t.get_viz_data())

        return json.dumps(data)


class ResearcherThemeRelationship(Orderable, models.Model):
    researcher = ParentalKey(
        'ResearcherPage', related_name='researcher_theme_relationship',
        on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'ThemePage', blank=True, null=True,
        related_name='theme_researcher_relationship', on_delete=models.CASCADE
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['projects'] = self.researcher_project_relationship.all(
        ).order_by('project__title')

        return context

    def get_page_facets(self):
        related = self.researcher_project_relationship.all()
        projects = ProjectPage.objects.live().filter(
            project_researcher_relationship__in=related).order_by('title')

        related = self.researcher_theme_relationship.all()
        themes = ThemePage.objects.live().filter(
            theme_researcher_relationship__in=related).order_by('title')

        secondary_themes = ThemePage.objects.none()

        for p in projects:
            secondary_themes = secondary_themes | p.get_themes()

        secondary_themes = secondary_themes.distinct()
        secondary_themes = secondary_themes.difference(themes)
        secondary_themes = secondary_themes.order_by('title')

        return [
            ('theme', themes),
            ('theme', secondary_themes),
            ('project', projects)
        ]

    def get_viz_data(self, related=True):
        data = {
            'class': 'researcher',
            'id': self.id,
            'title': self.title,
            'url': self.url
        }

        if related:
            data['related'] = []

            for related in self.researcher_project_relationship.filter(
                    project__depth=4):
                data['related'].append(
                    related.project.get_viz_data(related=False))

            for related in self.researcher_theme_relationship.all():
                if related.theme:
                    data['related'].append(
                        related.theme.get_viz_data(related=False))

        return data


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

    def has_bibliography(self):
        return self.endnotes.exclude(
            bibliography_entry__isnull=True).count() > 0


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
    full_title = models.CharField(max_length=512, blank=True, null=True)

    content_panels = BaseTimelinePage.content_panels + [
        InlinePanel('endnotes', label='EndNotes'),
        InlinePanel('project_theme_relationship',
                    label='Themes', panels=None, min_num=1),
        InlinePanel('project_researcher_relationship',
                    label='Researchers', panels=None, min_num=1),
    ] + FacetsMixin.content_panels

    parent_page_types = [IndexPage, 'ProjectPage']
    subpage_types = ['ProjectPage']

    def get_full_title(self):
        titles = []

        for page in self.get_ancestors().specific():
            if isinstance(page, ProjectPage):
                titles.append(page.title)

        titles.append(self.title)

        return ' > '.join(titles)

    def get_page_facets(self):
        related = self.project_researcher_relationship.all()
        researchers = ResearcherPage.objects.live().filter(
            researcher_project_relationship__in=related).order_by('title')

        return [
            ('theme', self.get_themes()),
            ('project',
             self.get_descendants().specific().live().order_by('title')),
            ('researcher', researchers)
        ]

    def get_themes(self):
        related = self.project_theme_relationship.all()
        return ThemePage.objects.live().filter(
            theme_project_relationship__in=related).order_by('title')

    def is_child(self):
        parent = self.get_parent().specific
        if isinstance(parent, ProjectPage):
            return True

        return False

    def get_viz_data(self, related=True):
        data = {
            'class': 'project',
            'id': self.id,
            'title': self.title,
            'url': self.url
        }

        if related:
            data['related'] = []

            for related in self.project_researcher_relationship.all():
                data['related'].append(
                    related.researcher.get_viz_data(related=False))

            for related in self.project_theme_relationship.all():
                data['related'].append(
                    related.theme.get_viz_data(related=False))

        return data


@receiver(pre_save, sender=ProjectPage)
def pp_pre_save(sender, instance, *args, **kwargs):
    instance.full_title = instance.get_full_title()


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
            project_theme_relationship__in=related).order_by('title')

        related = self.theme_researcher_relationship.all()
        researchers = ResearcherPage.objects.live().filter(
            researcher_theme_relationship__in=related).order_by('title')

        return [
            ('project', projects),
            ('researcher', researchers)
        ]

    def get_viz_data(self, related=True):
        data = {
            'class': 'theme',
            'id': self.id,
            'title': self.title,
            'url': self.url
        }

        if related:
            data['related'] = []

            for related in self.theme_researcher_relationship.all():
                data['related'].append(
                    related.researcher.get_viz_data(related=False))

            for related in self.theme_project_relationship.filter(
                    project__depth=4):
                data['related'].append(
                    related.project.get_viz_data(related=False))

        return data


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
