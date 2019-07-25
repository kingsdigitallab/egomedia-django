from django.core.management.base import BaseCommand
from core.models import ProjectPage


class Command(BaseCommand):
    help = 'Sets the full title field in Project pages'

    def handle(self, *args, **options):
        for pp in ProjectPage.objects.all():
            pp.save()
