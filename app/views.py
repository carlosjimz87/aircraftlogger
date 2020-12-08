from django.db.models import *
from rest_framework import viewsets, views
from rest_framework.response import Response

from app.models import Aircraft, Flight, Airport
from app.serializers import AircraftSerializer, FlightSerializer, ReadFlightSerializer, AirportSerializer, ReportSerializer
from django_filters import rest_framework as filters
from app.filters import FlightFilter


class AirportViewSet(viewsets.ModelViewSet):
    """
    Display a list of :model:`app.Airport` full data.
    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    """
    Display a list of :model:`app.Aircraft` full data.
    """
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    Display a list of :model:`app.Aircraft` full data.
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightFilter

    def get_serializer_class(self):
        """
        Choose :serializer:`app.ReadFlightSerializer`. for `list` and `retrieve` actions and
        :serializer:`app.FlightSerializer` for the rest
        """
        if self.action == 'list' or self.action == 'retrieve':
            return ReadFlightSerializer
        else:
            return super(FlightViewSet, self).get_serializer_class()


class ReportView(views.APIView):
    """
    Display a list of  :model:`app.Aiport`.
    with the number of  :model:`app.Flight` and the average in-time-flight for each one.
    """

    def get(self, request, format=None):
        """
        Creates a special query to show in the report: 

        -> Allow to get all departure airports by time
        (departure and arrival interval as required, provided as request param)...
        and for each airport the number of flights and in-flight times for each aircraft
        (this range time strictly within the time range of the search and the average in minutes). <-
        """
        time_from = request.query_params.get('departure_time_from')
        time_to = request.query_params.get('arrival_time_to')
        qs = Airport.objects.all()
        if time_from:
            qs = qs.filter(flights_departure__departure_time__gte=time_from)
        if time_to:
            qs = qs.filter(flights_departure__arrival_time__lte=time_to)
        qs = qs.annotate(flight_count=Count('flights_departure__id'), inflight_avg=Avg(
            "flights_departure__inflight_time"))
        qs = qs.filter(flight_count__gt=0)
        return Response(ReportSerializer(qs, many=True).data)
