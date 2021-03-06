from kdl_wagtail.core.blocks import (
    BaseCaptionAttributionBlock, BaseStreamBlock, BaseStructBlock,
    DocumentBlock, EmbedBlock, ImageBlock, LinkBlock, RichTextBlock,
    TableBlock
)
from wagtail.core.blocks import (
    CharBlock, ListBlock, StreamBlock, StructBlock, URLBlock
)


class MapBlock(BaseCaptionAttributionBlock):
    map_url = URLBlock()

    class Meta:
        icon = 'site'
        template = 'core/blocks/map_block.html'


class ModalBlock(BaseStructBlock):
    title = CharBlock()
    body = StreamBlock([
        ('description', RichTextBlock(required=False)),
        ('document_block', DocumentBlock(required=False)),
        ('embed_block', EmbedBlock(required=False)),
        ('image_block', ImageBlock(required=False)),
        ('map_block', MapBlock(required=False)),
        ('table_block', TableBlock(required=False))
    ])

    class Meta:
        icon = 'no-view'
        template = 'core/blocks/modal_block.html'


class TimelineItemBlock(StructBlock):
    title = CharBlock()
    # TODO possibly add a tag field, but wait for the meeting for feedback
    item = StreamBlock([
        ('description', RichTextBlock(required=False)),
        ('document_block', DocumentBlock(required=False)),
        ('image_block', ImageBlock(required=False)),
        ('link_block', LinkBlock(required=False)),
        ('embed_block', EmbedBlock(required=False))
    ])

    class Meta:
        icon = 'list-ol'
        template = 'core/blocks/timeline_item_block.html'


class TimelineBlock(BaseStructBlock):
    title = CharBlock()
    items = ListBlock(TimelineItemBlock())

    class Meta:
        icon = 'list-ol'
        template = 'core/blocks/timeline_block.html'


class HomePageStreamBlock(StreamBlock):
    richtext_block = RichTextBlock(
        icon='pilcrow',
        template='kdl_wagtail_core/blocks/richtext_block.html'
    )
    link_block = LinkBlock(required=False)
    timeline_block = ListBlock(TimelineBlock(), icon='list-ol')


class TimelineStreamBlock(BaseStreamBlock):
    map_block = MapBlock()
    modal_block = ModalBlock()
    timeline_block = TimelineBlock()
