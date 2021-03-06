# Generated by Django 2.1.5 on 2019-02-05 15:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('kdl_wagtail_people', '0005_personpage'),
        ('core', '0003_alter_field_body_on_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearcherPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page')),
                ('body', wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('heading_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')]))])), ('richtext_block', wagtail.core.blocks.RichTextBlock(icon='pilcrow', template='kdl_wagtail_core/blocks/richtext_block.html')), ('document_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('document', wagtail.documents.blocks.DocumentChooserBlock(required=True))])), ('gallery_block', wagtail.core.blocks.StructBlock([('images_block', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('image_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('link_block', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock())])), ('embed_block', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL', icon='media'))])), ('table_block', wagtail.contrib.table_block.blocks.TableBlock())], blank=True, verbose_name='Page body')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='researcher_pages', to='kdl_wagtail_people.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
