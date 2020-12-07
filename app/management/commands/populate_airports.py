from django.core.management.base import BaseCommand, CommandError
from app.utils import populate_airports


class Command(BaseCommand):
    help = 'Populate Airports (codes,names and cities) in DB.'

    def handle(self, *args, **options):

        try:
            airports = populate_airports()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created %d Airports.' % len(airports)))

        except Exception as err:
            self.stdout.write(self.style.ERROR("Error creating airports."))
