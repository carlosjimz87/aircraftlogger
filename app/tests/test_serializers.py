from app.serializers import WriteFlightSerializer
from . import *


class Serializers(BaseTest):
    def test_aircraft_serializer(self):
        aircrafts = Aircraft.objects.all()

        aircraft_serialized = AircraftSerializer(aircrafts, many=True)

        for pair in zip(self.aircraft_defaults, aircraft_serialized.data):
            self.assertEqual(pair[0], pair[1])

    def test_flight_serializer(self):
        flights = Flight.objects.all()

        flight_serialized = ReadFlightSerializer(flights, many=True)

        for pair in zip(self.flight_defaults, flight_serialized.data):
            self.assertEqual(pair[0]["departure"], pair[1]["departure"])
            self.assertEqual(pair[0]["arrival"], pair[1]["arrival"])

            # testing nested aircrafts fields
            self.assertEqual(pair[0]["aircraft"].serial_number,
                             pair[1]["aircraft"]["serial_number"])
            self.assertEqual(pair[0]["aircraft"].manufacturer,
                             pair[1]["aircraft"]["manufacturer"])
