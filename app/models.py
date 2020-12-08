from django.db import models


class Airport(models.Model):
    """
    Stores an airport entry.
    Fields:
        - icao_code
        - city
        - name
    """
    icao_code = models.CharField(max_length=4, primary_key=True)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return 'Airport({},{},{})'.format(self.icao_code, self.city, self.name)


class Aircraft(models.Model):
    """
    Stores an aircraft entry.
    Fields:
        - serial_number
        - manufacturer
    """
    serial_number = models.CharField(max_length=6, primary_key=True)
    manufacturer = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Aircrafts"

    def __str__(self):
        return 'Aircraft({},{})'.format(self.serial_number, self.manufacturer)


class Flight(models.Model):
    """
    Stores a flight entry.
    Fields:
        - departure (related to :model:`app.Airport`)
        - arrival (related to :model:`app.Airport`)
        - aircraft (related to :model:`app.Aircraft`)
        - departure_time
        - arrival_time
    """
    departure = models.ForeignKey(Airport, related_name='flights_departure', on_delete=models.CASCADE)
    arrival = models.ForeignKey(Airport, related_name='flights_arrival', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey(Aircraft, related_name='flights', on_delete=models.CASCADE, null=True)
    inflight_time = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Flights"

    def __str__(self):
        return 'Flight({},{},{})'.format(self.departure, self.arrival, self.aircraft)

    def save(self, *args, **kwargs):
        """
        Before to save a flight in the database,
        it calculates an `inflight_time` property from `arrival_time` and `departure_time`
        as the following: ` inflight_time = round((arrival_time - departure_time) / 60 )`
        """
        self.inflight_time = round((self.arrival_time-self.departure_time).seconds/60)
        return super(Flight, self).save(*args, **kwargs)
