from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from app.models import Aircraft, Flight
from app.serializers import AircraftSerializer, FlightSerializer
from django.utils.timezone import now
from datetime import timedelta
from app.utils import populate_airports


class BaseTest(TestCase):
    def setUp(self) -> None:
        # region Models & Serializers
        aiports = populate_airports(20)

        self.aircraft_defaults = [
            dict(serial_number="AA5435", manufacturer="Airbus"),
            dict(serial_number="BA2311", manufacturer="Boeing"),
            dict(serial_number="EM8799", manufacturer="Embraer"),
        ]
        aircraft_objects = [Aircraft.objects.create(
            **aircraft) for aircraft in self.aircraft_defaults]

        self.flight_defaults = [
            dict(departure=aiports[0],
                 arrival=aiports[1],
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=3),
                 aircraft=aircraft_objects[0]
                 ),
            dict(departure=aiports[2],
                 arrival=aiports[3],
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=6),
                 aircraft=aircraft_objects[1]
                 ),
            dict(departure=aiports[4],
                 arrival=aiports[5],
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=8),
                 aircraft=aircraft_objects[2]
                 ),
        ]

        [Flight.objects.create(
            **flight) for flight in self.flight_defaults]

        # endregion

        # region Validators
        self.invalidDepartureTimeData = dict(departure=aiports[6],
                                             arrival=aiports[7],
                                             departure_time=now()-timedelta(hours=1),   # this time should raise an error
                                             arrival_time=now()+timedelta(hours=3),
                                             aircraft=Aircraft.objects.first()
                                             )

        self.invalidArrivalTimeData = dict(departure=aiports[8],
                                           arrival=aiports[9],
                                           departure_time=now(),   # this time should raise an error
                                           arrival_time=now()-timedelta(hours=3),
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
            departure=aiports[10].icao_code,
            arrival=aiports[11].icao_code,
            departure_time="2020-12-21T23:03:00Z",
            arrival_time="2020-12-22T23:03:00Z",
            aircraft=self.aircraft_defaults[0]["serial_number"]
        )
        # endregion
