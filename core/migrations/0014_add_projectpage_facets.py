# Generated by Django 2.1.5 on 2019-02-07 15:31

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_add_themepage_facets'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='disciplines',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.Discipline'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='focus',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.Focus'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='keywords',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.Keyword'),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='methods',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='core.Method'),
        ),
    ]
