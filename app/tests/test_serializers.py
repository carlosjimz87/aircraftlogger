from . import *


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
            self.assertEqual(pair[0]["departure"].icao_code,
                             pair[1]["departure"])
            self.assertEqual(pair[0]["arrival"].icao_code,
                             pair[1]["arrival"])

            # testing nested aircrafts fields
            self.assertEqual(pair[0]["aircraft"].serial_number,
                             pair[1]["aircraft"])

    def test_invalid_departure_time(self):
        flight_serialized = FlightSerializer(
            data=self.invalidDepartureTimeData)
        self.assertFalse(flight_serialized.is_valid())

    def test_invalid_arrival_time(self):
        flight_serialized = FlightSerializer(data=self.invalidArrivalTimeData)
        self.assertFalse(flight_serialized.is_valid())
