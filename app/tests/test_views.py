from . import *


class TestViews(BaseTest):

    def test_aircraft_list_get(self):
        res = self.client.get(self.urls.get("aircraft_list"))
        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.data, self.aircraft_defaults)

    def test_flight_list_get(self):
        res = self.client.get(self.urls.get("flight_list"))
        self.assertEquals(res.status_code, 200)

        for pair in zip(self.flight_defaults, res.data):
            self.assertEqual(pair[0]["departure"].icao_code,
                             pair[1]["departure"]["icao_code"])
            self.assertEqual(pair[0]["arrival"].icao_code,
                             pair[1]["arrival"]["icao_code"])

            # testing nested aircrafts fields
            self.assertEqual(pair[0]["aircraft"].serial_number,
                             pair[1]["aircraft"]["serial_number"])
            self.assertEqual(pair[0]["aircraft"].manufacturer,
                             pair[1]["aircraft"]["manufacturer"])

    def test_aircraft_list_post(self):
        res = self.client.post(self.urls.get(
            "aircraft_list"), self.aircraft_post_data)
        self.assertEquals(res.status_code, 201)

    def test_flight_list_post(self):
        res = self.client.post(self.urls.get(
            "flight_list"), self.flight_post_data)
        self.assertEquals(res.status_code, 201)

    def test_report_view(self):
        res = self.client.get(self.urls.get("report_list"),)
        self.assertEquals(len(res.data), 5)
        self.assertEquals(res.status_code, 200)

    def test_report_view_with_daterange_for_two_last_flights(self):
        res = self.client.get(self.urls.get("report_list"), self.range_for_report_for_two_last_flights)
        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.data[0]["flight_count"], 2)
        self.assertEquals(res.data[0]["inflight_avg"], 600.0)


