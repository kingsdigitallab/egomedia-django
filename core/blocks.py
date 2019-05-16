from kdl_wagtail.core.blocks import (
    BaseCaptionAttributionBlock, BaseStreamBlock, BaseStructBlock,
    DocumentBlock, EmbedBlock, ImageBlock, LinkBlock, TableBlock
)
from kdl_wagtail.zotero.models import Bibliography
from wagtail.core.blocks import (
    BooleanBlock, CharBlock, ListBlock, RichTextBlock, StreamBlock,
    StructBlock, URLBlock
)
from wagtail.snippets.blocks import SnippetChooserBlock


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


class EndNoteItemBlock(StreamBlock):
    richtext_block = RichTextBlock(
        icon='pilcrow', required=False,
        template='kdl_wagtail_core/blocks/richtext_block.html'
    )
    bibliography_block = StructBlock([
        ('entry', SnippetChooserBlock(Bibliography, required=True)),
        ('pages', CharBlock(required=False)),
        ('shortnote', BooleanBlock(required=False))
    ], icon='form', required=False)

    class Meta:
        icon = 'list-ol'
        template = 'core/blocks/endnote_block.html'


class EndNoteStreamBlock(StreamBlock):
    note_block = EndNoteItemBlock()


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
