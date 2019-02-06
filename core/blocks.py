from kdl_wagtail.core.blocks import (BaseStreamBlock, DocumentBlock,
                                     EmbedBlock, ImageBlock, LinkBlock)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks import (CharBlock, ListBlock, RichTextBlock,
                                 StreamBlock, StructBlock)


class AnnotationBlock(StructBlock):
    title = CharBlock()
    body = StreamBlock([
        ('description', RichTextBlock(required=False)),
        ('document_block', DocumentBlock(required=False)),
        ('image_block', ImageBlock(required=False)),
        ('embed_block', EmbedBlock(required=False)),
        ('table_block', TableBlock(required=False))
    ])

    class Meta:
        icon = 'no-view'
        template = 'core/blocks/annotation_block.html'


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


class TimelineBlock(StructBlock):
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
    # TODO rename this sequence instead of timeline
    annotation_block = AnnotationBlock()
    timeline_block = TimelineBlock()
