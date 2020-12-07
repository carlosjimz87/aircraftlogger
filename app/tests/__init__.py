from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from app.models import Aircraft, Flight
from app.serializers import AircraftSerializer, FlightSerializer
from django.utils.timezone import now
from datetime import timedelta


class BaseTest(TestCase):
    def setUp(self) -> None:
        # region Models & Serializers

        self.aircraft_defaults = [
            dict(serial_number="AA5435", manufacturer="Airbus"),
            dict(serial_number="BA2311", manufacturer="Boeing"),
            dict(serial_number="EM8799", manufacturer="Embraer"),
        ]
        aircraft_objects = [Aircraft.objects.create(
            **aircraft) for aircraft in self.aircraft_defaults]

        self.flight_defaults = [
            dict(departure="CYYT",
                 arrival="CYYJ",
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=3),
                 aircraft=aircraft_objects[0]
                 ),
            dict(departure="EDDG",
                 arrival="EDDH",
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=6),
                 aircraft=aircraft_objects[1]
                 ),
            dict(departure="SBCF",
                 arrival="SBCT",
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=8),
                 aircraft=aircraft_objects[2]
                 ),
        ]

        [Flight.objects.create(
            **flight) for flight in self.flight_defaults]

        # endregion

        # region Validators
        self.invalidFlightData = dict(departure="SUMU",
                                      arrival="SVBC",
                                      departure_time=now()-timedelta(hours=1),   # this time should raise an error
                                      arrival_time=now()+timedelta(hours=3),
                                      aircraft=Aircraft.objects.first()
                                      )

        # endregion

        # region Views & Urls

        # default router urls
        self.urls = dict(
            aircraft_list=reverse('aircraft-list'),
            aircraft_detail=reverse('aircraft-detail', args=[1]),
            flight_list=reverse('flight-list'),
            flight_detail=reverse('flight-detail', args=[1]),
        )

        self.aircraft_post_data = dict(
            serial_number="AE9882", manufacturer="BAE"
        )

        self.flight_post_data = dict(
            departure="UKFF",
            arrival="UKOO",
            departure_time="2020-12-21T23:03:00Z",
            arrival_time="2020-12-22T23:03:00Z",
            aircraft=self.aircraft_defaults[0]["serial_number"]
        )
        # endregion
