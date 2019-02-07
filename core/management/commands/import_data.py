import csv

from core.models import HomePage, Keyword, ThemePage
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from kdl_wagtail.core.models import IndexPage


class Command(BaseCommand):
    help = 'Imports themes, researchers and projects from the CSVs in data'

    def handle(self, *args, **options):
        self.import_themes_and_researchers('data/themes.csv')

    def import_themes_and_researchers(self, csv_filename):
        themes_index_page = self.get_or_create_themes_index_page()

        with open(csv_filename) as csvfile:
            themes_reader = csv.reader(csvfile)

            for row in themes_reader:
                title = row[0].strip()

                try:
                    theme_page = ThemePage.objects.get(title=title)
                except ThemePage.DoesNotExist:
                    theme_page = ThemePage(title=title, slug=slugify(title))

                    themes_index_page.add_child(instance=theme_page)

                    theme_page.save()
                    revision = theme_page.save_revision()
                    revision.publish()

                keywords_list = row[3].split(';')
                for title in keywords_list:
                    title = title.strip().lower()
                    if title:
                        keyword, _ = Keyword.objects.get_or_create(title=title)
                        theme_page.keywords.add(keyword)

                theme_page.save()

    def get_or_create_themes_index_page(self):
        try:
            themes_index_page = IndexPage.objects.get(title='Themes')
        except IndexPage.DoesNotExist:
            themes_index_page = IndexPage(title='Themes', slug='themes')

            home_page = HomePage.objects.first()
            home_page.add_child(instance=themes_index_page)

            themes_index_page.save()

            revision = themes_index_page.save_revision()
            revision.publish()

        return themes_index_page
