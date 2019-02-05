from base.blocks import HomePageStreamBlock
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.search import index


class HomePage(Page):
    body = StreamField(HomePageStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    subpage_types = ['GenericPage', 'IndexPage']
