from kdl_wagtail.core.blocks import (BaseStreamBlock, DocumentBlock,
                                     EmbedBlock, ImageBlock, LinkBlock)
from wagtail.core.blocks import (CharBlock, ListBlock, RichTextBlock,
                                 StreamBlock, StructBlock, TextBlock)


# TODO add block similar to timeline block, the options are text (richtext)
# and one of document, image, link, embed, table

class TimelineBlock(StructBlock):
    # TODO rename this to node title
    title = CharBlock()
    # TODO remove this field
    label = CharBlock()
    # TODO add a tag field, but wait for the meeting for feedback
    item = StreamBlock([
        # TODO convert description to rich text
        ('description', TextBlock(required=False)),
        ('document_block', DocumentBlock(required=False)),
        ('image_block', ImageBlock(required=False)),
        ('link_block', LinkBlock(required=False)),
        ('embed_block', EmbedBlock(required=False))
    ])

    class Meta:
        icon = 'list-ol'
        template = 'core/blocks/timeline_block.html'


class HomePageStreamBlock(StreamBlock):
    richtext_block = RichTextBlock(
        icon='pilcrow',
        template='kdl_wagtail/blocks/richtext_block.html'
    )
    link_block = LinkBlock(required=False)
    timeline_block = ListBlock(TimelineBlock(), icon='list-ol')


class TimelineStreamBlock(BaseStreamBlock):
    # TODO rename this sequence instead of timeline
    # TODO add a title field
    timeline_block = ListBlock(TimelineBlock(), icon='list-ol')
