# Generated by Django 2.2.1 on 2019-05-21 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_endnotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='endnotes',
        ),
        migrations.RemoveField(
            model_name='themepage',
            name='endnotes',
        ),
    ]