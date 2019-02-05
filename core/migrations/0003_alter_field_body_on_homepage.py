# Generated by Django 2.1.5 on 2019-02-05 15:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_field_body_on_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('richtext_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='kdl_wagtail/blocks/richtext_block.html')), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('timeline_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('label', wagtail.core.blocks.CharBlock()), ('item', wagtail.core.blocks.StreamBlock([('description', wagtail.core.blocks.TextBlock(required=False)), ('document_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))], required=False)), ('image_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))], required=False)), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())], required=False)), ('embed_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))], required=False))]))]), icon='list-ol'))]),
        ),
    ]
