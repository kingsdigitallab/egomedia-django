# Generated by Django 2.1.5 on 2019-02-07 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_add_researcherpage_facets'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='focus',
            options={'ordering': ['title'], 'verbose_name_plural': 'Focus'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='method',
            options={'ordering': ['title']},
        ),
    ]
