from core.blocks import HomePageStreamBlock, TimelineStreamBlock
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index
from kdl_wagtail.people.models import Person, PersonModel
from kdl_wagtail.core.models import BasePage, BaseStreamPage
from django.db import models
from wagtail.api import APIField
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class HomePage(Page):
    body = StreamField(HomePageStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]


class ResearcherPage(BaseStreamPage):
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
    pass


class ThemePage(BaseTimelinePage):
    pass
