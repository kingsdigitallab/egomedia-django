# Generated by Django 2.2.5 on 2019-09-26 10:42

from django.db import migrations
import kdl_wagtail.core.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_change_meta_options_on_facet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('richtext_block', kdl_wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='kdl_wagtail_core/blocks/richtext_block.html')), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('timeline_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('title', wagtail.core.blocks.CharBlock()), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('item', wagtail.core.blocks.StreamBlock([('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False))]))])))]), icon='list-ol'))]),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')]))])), ('richtext_block', kdl_wagtail.core.blocks.RichTextBlock()), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('gallery_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())])), ('pullquote_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('quote', kdl_wagtail.core.blocks.RichTextBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))])), ('table_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))])), ('map_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())])), ('modal_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.StreamBlock([('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('map_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())], required=False)), ('table_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))], required=False))]))])), ('timeline_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('title', wagtail.core.blocks.CharBlock()), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('item', wagtail.core.blocks.StreamBlock([('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False))]))])))]))], blank=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='researcherpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')]))])), ('richtext_block', kdl_wagtail.core.blocks.RichTextBlock()), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('gallery_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())])), ('pullquote_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('quote', kdl_wagtail.core.blocks.RichTextBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))])), ('table_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))]))], blank=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='themepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')]))])), ('richtext_block', kdl_wagtail.core.blocks.RichTextBlock()), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('gallery_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())])), ('pullquote_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('quote', kdl_wagtail.core.blocks.RichTextBlock()), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))])), ('table_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))])), ('map_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())])), ('modal_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.StreamBlock([('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('map_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('map_url', wagtail.core.blocks.URLBlock())], required=False)), ('table_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(required=True))], required=False))]))])), ('timeline_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('title', wagtail.core.blocks.CharBlock()), ('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('item', wagtail.core.blocks.StreamBlock([('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(help_text='Link to a page', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='External link', required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select block alignment'), ('float-left', 'Left'), ('float-right', 'Right'), ('float-center', 'Centre'), ('full-width', 'Full width')])), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('link_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('show_in_menus', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('transcription', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('description', kdl_wagtail.core.blocks.RichTextBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('display', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a display ratio'), ('widescreen', '16:9'), ('fourbythree', '4:3'), ('audio', 'Audio'), ('panorama', 'Panorama'), ('square', 'Square'), ('vertical', 'Vertical')], required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False))]))])))]))], blank=True, verbose_name='Page body'),
        ),
    ]
