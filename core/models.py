from base.blocks import GenericStreamBlock, HomePageStreamBlock
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from kdl_wagtail.models import StandardPage
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index


class GenericPage(Page):
    introduction = models.TextField(
        help_text='Text to describe the page', blank=True
    )
    image = models.ForeignKey(
        Image, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(GenericStreamBlock(),
                       verbose_name='Page body', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname='full'),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
        index.SearchField('body')
    ]


class HomePage(Page):
    body = StreamField(HomePageStreamBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body')
    ]

    subpage_types = ['GenericPage', 'IndexPage']


class IndexPage(StandardPage):
    subpage_types = ['GenericPage', 'IndexPage']

    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super().get_context(request)

        children = self.paginate(request, self.children())

        context['children'] = children

        return context

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.children(), settings.ITEMS_PER_PAGE)

        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        return pages
