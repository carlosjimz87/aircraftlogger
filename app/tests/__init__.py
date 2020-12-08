from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from app.models import Aircraft, Flight
from django.utils.timezone import now
from datetime import timedelta
from app.serializers import *
from app.utils import populate_airports, populate_aircrafts, populate_flights


class BaseTest(TestCase):
    def setUp(self) -> None:
        # region Models & Serializers
        airports = populate_airports(20)

        self.aircraft_defaults, aircrafts = populate_aircrafts()

        self.flight_defaults, _ = populate_flights(airports, aircrafts)
        # endregion

        # region Validators
        self.invalidDepartureTimeData = dict(departure=airports[6],
                                             arrival=airports[7],
                                             departure_time=now() - timedelta(hours=1),
                                             # this time should raise an error
                                             arrival_time=now() + timedelta(hours=3),
                                             aircraft=Aircraft.objects.first()
                                             )

        self.invalidArrivalTimeData = dict(departure=airports[8],
                                           arrival=airports[9],
                                           departure_time=now(),  # this time should raise an error
                                           arrival_time=now() - timedelta(hours=3),
                                           aircraft=Aircraft.objects.first()
                                           )

        # endregion

        # region Views & Urls

        # default router urls
        self.urls = dict(
            report_list=reverse('report-list'),
            aircraft_list=reverse('aircraft-list'),
            aircraft_detail=reverse('aircraft-detail', args=[1]),
            flight_list=reverse('flight-list'),
            flight_detail=reverse('flight-detail', args=[1]),
        )

        self.aircraft_post_data = dict(
            serial_number="AE9882", manufacturer="BAE"
        )

        self.flight_post_data = dict(
            departure=airports[10].icao_code,
            arrival=airports[11].icao_code,
            departure_time="2020-12-21T23:03:00Z",
            arrival_time="2020-12-22T23:03:00Z",
            aircraft=aircrafts[0].serial_number
        )
        self.range_for_report_for_two_last_flights = dict(
            departure_time_from=now() + timedelta(days=3),
            arrival_time_to=now() + timedelta(days=6),  # inflight_time = 8h
        )

        # endregion
