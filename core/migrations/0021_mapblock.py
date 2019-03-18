# Generated by Django 2.1.7 on 2019-03-13 11:27

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_add_modalblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')]))])), ('richtext_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='kdl_wagtail_core/blocks/richtext_block.html')), ('document_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('gallery_block', wagtail.core.blocks.StructBlock([('images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('image_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())])), ('embed_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))])), ('table_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))])), ('openstreetmap_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())])), ('modal_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.StreamBlock([('description', wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('openstreetmap_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())], required=False)), ('table_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))], required=False))]))])), ('timeline_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('item', wagtail.core.blocks.StreamBlock([('description', wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False))]))])))]))], blank=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='themepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')]))])), ('richtext_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='kdl_wagtail_core/blocks/richtext_block.html')), ('document_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('gallery_block', wagtail.core.blocks.StructBlock([('images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('image_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())])), ('embed_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))])), ('table_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))])), ('openstreetmap_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())])), ('modal_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.StreamBlock([('description', wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('openstreetmap_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())], required=False)), ('table_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))], required=False))]))])), ('timeline_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('item', wagtail.core.blocks.StreamBlock([('description', wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('left', 'Left'), ('right', 'Right'), ('center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('transcription', wagtail.core.blocks.RichTextBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False))]))])))]))], blank=True, verbose_name='Page body'),
        ),
    ]