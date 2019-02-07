# Generated by Django 2.1.5 on 2019-02-07 17:23

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_add_projectpage_facets'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectResearcherRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('project', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_researcher_relationship', to='core.ProjectPage')),
                ('researcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='researcher_project_relationship', to='core.ResearcherPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='ProjectThemeRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('project', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_theme_relationship', to='core.ProjectPage')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme_project_relationship', to='core.ThemePage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
