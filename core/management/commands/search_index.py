import os
import sys

from core.models import TextSearchPage
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Creates or updates the Lunr search index'

    def handle(self, *args, **options):
        self.stdout.write('Creating search data...')
        with open('assets/js/search_data.json', 'w') as f:
            f.write(TextSearchPage.get_search_data())
            f.close()

        self.stdout.write('Generating search index...')
        try:
            sys.stdout.flush()
            os.execvp('node', ['node', 'assets/js/search_builder.js'])
        except OSError as e:
            self.stderr.write('Error generating search index')
            raise CommandError(e)
