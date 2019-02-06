from core.blocks import HomePageStreamBlock, TimelineStreamBlock
from django.db import models
from kdl_wagtail.core.models import (BasePage, BaseStreamPage, IndexPage,
                                     RichTextPage, StreamPage)
from kdl_wagtail.people.models import (PeopleIndexPage, Person, PersonModel,
                                       PersonPage)
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.api import APIField
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


class BaseFacet(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        abstract = True

    def str(self):
        return self.title


@register_snippet
class Discipline(BaseFacet):
    pass


@register_snippet
class Focus(BaseFacet):
    class Meta:
        verbose_name_plural = 'Focus'


@register_snippet
class Keyword(BaseFacet):
    pass


@register_snippet
class Method(BaseFacet):
    pass


class HomePage(Page):
    body = StreamField(HomePageStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    subpage_types = [IndexPage, PeopleIndexPage, StreamPage]


class ResearcherPage(BaseStreamPage):
    # TODO add links to facets
    # TODO add link to themes
    person = models.ForeignKey(
        PersonModel, related_name='researcher_pages', on_delete=models.PROTECT)

    api_fields = BaseStreamPage.api_fields + [
        APIField('person')
    ]

    content_panels = BaseStreamPage.content_panels + [
        SnippetChooserPanel('person')
    ]

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


class ProjectPage(BaseTimelinePage):
    # TODO add links to facets
    # TODO add link to person

    parent_page_types = [IndexPage, 'ProjectPage']
    subpage_types = ['ProjectPage']


class ThemePage(BaseTimelinePage):
    # TODO add links to facets
    # TODO add link to themes

    parent_page_types = [IndexPage]
    subpage_types = []


# TODO add snippets for keyword, focus, method, discipline

# Sets up pages' visibility
IndexPage.parent_page_types = [HomePage, IndexPage]
IndexPage.subpage_types = [IndexPage, ProjectPage, StreamPage, ThemePage]
PeopleIndexPage.parent_page_types = [HomePage]
PeopleIndexPage.subpage_types = [ResearcherPage]
PersonPage.parent_page_types = []
PersonPage.subpage_types = []
ProjectPage.subpage_types = [ProjectPage]
RichTextPage.parent_page_types = []
RichTextPage.subpage_types = []
StreamPage.parent_page_types = [HomePage, IndexPage]

# Re-label the stream page to match the name required by this project
StreamPage._meta.verbose_name = 'Generic page'
StreamPage._meta.verbose_name_plural = 'Generic pages'
