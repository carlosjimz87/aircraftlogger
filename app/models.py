from django.db import models
from django.db.models.fields import CharField
from django.conf import settings


def get_airport_codes():
    with open(settings.MEDIA_ROOT / "airports") as f:
        return [[line, line] for line in f.read().splitlines()]


class Aircraft(models.Model):
    serial_number = models.CharField(max_length=6)
    manufacturer = models.CharField(max_length=20)

    class Meta:
        ordering = ['manufacturer']


class Flight(models.Model):
    departure = models.CharField(choices=get_airport_codes(), max_length=4)
    arrival = models.CharField(choices=get_airport_codes(), max_length=4)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey(
        Aircraft, related_name='flights', on_delete=models.CASCADE)

    class Meta:
        ordering = ['departure_time', 'arrival_time']
