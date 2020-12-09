from django.core.management.base import BaseCommand, CommandError
from app.utils import populate_aircrafts, populate_airports, populate_flights


class Command(BaseCommand):
    help = 'Populate database with dummy data.'

    def handle(self, *args, **options):

        try:
            airports = populate_airports()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created %d Airports.' % len(airports)))

            _, aircrafts = populate_aircrafts()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created %d Aircrafts.' % len(aircrafts)))

            _, flights = populate_flights(airports, aircrafts)
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created %d Flights.' % len(flights)))

        except Exception as err:
            self.stdout.write(self.style.ERROR(
                "Error populating database."+err))
