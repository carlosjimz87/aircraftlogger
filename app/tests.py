from django.test import TestCase
from app.models import Aircraft, Flight
from app.serializers import AircraftSerializer, FlightSerializer
from django.utils.timezone import now
from datetime import timedelta
from datetime import datetime


class BaseTest(TestCase):
    def setUp(self) -> None:
        self.aircraft_defaults = [
            dict(serial_number="AA5435", manufacturer="Airbus"),
            dict(serial_number="BA2311", manufacturer="Boeing"),
            dict(serial_number="EM8799", manufacturer="Embraer"),
        ]
        aircraft_objects = [Aircraft.objects.create(
            **aircraft) for aircraft in self.aircraft_defaults]

        self.flight_defaults = [
            dict(departure="00AA",
                 arrival="00AK",
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=3),
                 aircraft=aircraft_objects[0]
                 ),
            dict(departure="KCGF",
                 arrival="KCHQ",
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=6),
                 aircraft=aircraft_objects[1]
                 ),
            dict(departure="SVBW",
                 arrival="SVCO",
                 departure_time=now(),
                 arrival_time=now()+timedelta(hours=8),
                 aircraft=aircraft_objects[2]
                 ),
        ]

        [Flight.objects.create(
            **flight) for flight in self.flight_defaults]


class Models(BaseTest):
    def test_aircrafts(self):
        aircrafts = Aircraft.objects.all()
        self.assertEqual(len(aircrafts), 3)

        for pair in zip(self.aircraft_defaults, aircrafts):
            self.assertEqual(pair[0]["serial_number"], pair[1].serial_number)
            self.assertEqual(pair[0]["manufacturer"], pair[1].manufacturer)

    def test_flights(self):
        flights = Flight.objects.all()
        self.assertEqual(len(flights), 3)

        for pair in zip(self.flight_defaults, flights):
            self.assertEqual(pair[0]["departure"], pair[1].departure)
            self.assertEqual(pair[0]["arrival"], pair[1].arrival)
            self.assertEqual(pair[0]["departure_time"], pair[1].departure_time)
            self.assertEqual(pair[0]["arrival_time"], pair[1].arrival_time)
            self.assertEqual(pair[0]["aircraft"], pair[1].aircraft)


class Serializers(BaseTest):
    def test_aircraft_serializer(self):
        aircrafts = Aircraft.objects.all()

        aircraft_serialized = AircraftSerializer(aircrafts, many=True)

        for pair in zip(self.aircraft_defaults, aircraft_serialized.data):
            self.assertEqual(pair[0], pair[1])

    def test_flight_serializer(self):
        flights = Flight.objects.all()

        flight_serialized = FlightSerializer(flights, many=True)

        for pair in zip(self.flight_defaults, flight_serialized.data):
            self.assertEqual(pair[0]["departure"], pair[1]["departure"])
            self.assertEqual(pair[0]["arrival"], pair[1]["arrival"])

            # testing nested aircrafts fields
            self.assertEqual(pair[0]["aircraft"].serial_number,
                             pair[1]["aircraft"]["serial_number"])
            self.assertEqual(pair[0]["aircraft"].manufacturer,
                             pair[1]["aircraft"]["manufacturer"])
