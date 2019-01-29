from kdl_wagtail.blocks import (BaseStreamBlock, DocumentBlock, EmbedBlock,
                                ImageBlock, LinkBlock)
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks import (CharBlock, ListBlock, RichTextBlock,
                                 StreamBlock, StructBlock, TextBlock)


class TimelineBlock(StructBlock):
    title = CharBlock()
    label = CharBlock()
    item = StreamBlock([
        ('description', TextBlock(required=False)),
        ('document_block', DocumentBlock(required=False)),
        ('image_block', ImageBlock(required=False)),
        ('link_block', LinkBlock(required=False)),
        ('embed_block', EmbedBlock(required=False))
    ])

    class Meta:
        icon = 'list-ul'
        template = 'base/blocks/timeline_block.html'


class GenericStreamBlock(BaseStreamBlock):
    table_block = TableBlock()


class HomePageStreamBlock(StreamBlock):
    richtext_block = RichTextBlock(
        icon='pilcrow',
        template='kdl_wagtail/blocks/richtext_block.html'
    )
    link_block = LinkBlock(required=False)
    timeline_block = ListBlock(TimelineBlock)
