import csv

from core.models import (HomePage, Keyword, ResearcherPage,
                         ResearcherThemeRelationship, ThemePage)
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from kdl_wagtail.core.models import IndexPage
from kdl_wagtail.people.models import (PeopleIndexPage,
                                       PeopleIndexPersonRelationship, Person)


class Command(BaseCommand):
    help = 'Imports themes, researchers and projects from the CSVs in data'

    def handle(self, *args, **options):
        self.import_themes_and_researchers('data/themes.csv')

    def import_themes_and_researchers(self, csv_filename):
        themes_index_page = self.get_or_create_themes_index_page()
        researchers_index_page = self.get_or_create_researchers_index_page()

        with open(csv_filename) as csvfile:
            themes_reader = csv.reader(csvfile)

            for i, row in enumerate(themes_reader):
                if i == 0:
                    continue

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

                self.import_researchers(
                    row, researchers_index_page, theme_page)

    def get_or_create_themes_index_page(self):
        title = 'Themes'

        try:
            themes_index_page = IndexPage.objects.get(title=title)
        except IndexPage.DoesNotExist:
            themes_index_page = IndexPage(title=title, slug=slugify(title))
            home_page = HomePage.objects.first()
            home_page.add_child(instance=themes_index_page)

        themes_index_page.save()

        revision = themes_index_page.save_revision()
        revision.publish()

        return themes_index_page

    def get_or_create_researchers_index_page(self):
        title = 'Researchers'

        try:
            researchers_index_page = PeopleIndexPage.objects.get(title=title)
        except PeopleIndexPage.DoesNotExist:
            researchers_index_page = PeopleIndexPage(
                title=title, slug=slugify(title))
            home_page = HomePage.objects.first()
            home_page.add_child(instance=researchers_index_page)

        researchers_index_page.save()

        revision = researchers_index_page.save_revision()
        revision.publish()

        return researchers_index_page

    def import_researchers(self, row, researchers_index_page, theme_page):
        researchers = row[1].split(';')

        for name in researchers:
            name = name.strip()
            if name:
                person, _ = Person.objects.get_or_create(name=name)

                pipr = PeopleIndexPersonRelationship(
                    page=researchers_index_page, person=person)
                pipr.save()

                try:
                    researcher_page = ResearcherPage.objects.get(title=name)
                except ResearcherPage.DoesNotExist:
                    researcher_page = ResearcherPage(title=name)
                    researcher_page.person = person
                    researchers_index_page.add_child(instance=researcher_page)

                researcher_page.save()
                revision = researcher_page.save_revision()
                revision.publish()

                rtr = ResearcherThemeRelationship(
                    researcher=researcher_page, theme=theme_page)
                rtr.save()
