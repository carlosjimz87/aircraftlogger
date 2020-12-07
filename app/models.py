from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.fields import CharField
from django.conf import settings
from app.validators import departure_time_validator, arrival_time_validator


def get_airport_codes():
    with open(settings.MEDIA_ROOT / "airports") as f:
        return [[line, line] for line in f.read().splitlines()]


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=6, primary_key=True)
    manufacturer = models.CharField(max_length=20)

    class Meta:
        ordering = ['manufacturer']
        verbose_name_plural = "Aircrafts"

    def __str__(self):
        return 'Aircraft({},{})'.format(self.serial_number, self.manufacturer)


class Flight(models.Model):
    departure = models.CharField(choices=get_airport_codes(), max_length=4)
    arrival = models.CharField(choices=get_airport_codes(), max_length=4)
    departure_time = models.DateTimeField(
        validators=[departure_time_validator])
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey(
        Aircraft, related_name='flights', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['departure_time', 'arrival_time']
        verbose_name_plural = "Flights"

    def __str__(self):
        return 'Flight({},{},{})'.format(self.departure, self.arrival, self.aircraft)

    def clean(self) -> None:
        arrival_time_validator(self)
        return super().clean()
