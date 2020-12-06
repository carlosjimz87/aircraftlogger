from . import *


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

    def test_invalid_departure_time(self):
        flight = Flight(**self.invalidFlightData)
        self.assertRaises(ValidationError, flight.full_clean)
