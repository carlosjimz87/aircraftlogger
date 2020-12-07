from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import CharField
from django.conf import settings
from app.validators import departure_time_validator, arrival_time_validator


def get_airport_codes():
    with open(settings.MEDIA_ROOT / "airports") as f:
        return [[line, line] for line in f.read().splitlines()]


class Airport(models.Model):
    icao_code = models.CharField(max_length=4, primary_key=True)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    #
    # class Meta:
    #     ordering = ['icao_code']
    #     verbose_name_plural = "Airports"

    def __str__(self):
        return 'Airport({},{},{})'.format(self.icao_code, self.city, self.name)


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=6, primary_key=True)
    manufacturer = models.CharField(max_length=20)

    class Meta:
        ordering = ['manufacturer']
        verbose_name_plural = "Aircrafts"

    def __str__(self):
        return 'Aircraft({},{})'.format(self.serial_number, self.manufacturer)


class Flight(models.Model):
    departure = models.ForeignKey(
        Airport, related_name='flights_departure', on_delete=models.CASCADE)
    arrival = models.ForeignKey(
        Airport, related_name='flights_arrival', on_delete=models.CASCADE)

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey(
        Aircraft, related_name='flights', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['departure_time', 'arrival_time']
        verbose_name_plural = "Flights"

    def __str__(self):
        return 'Flight({},{},{})'.format(self.departure, self.arrival, self.aircraft)
