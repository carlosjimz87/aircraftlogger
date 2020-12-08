from django.db.models import *
from rest_framework import viewsets, views
from rest_framework.response import Response

from app.models import Aircraft, Flight, Airport
from app.serializers import AircraftSerializer, FlightSerializer, ReadFlightSerializer, AirportSerializer, ReportSerializer
from django_filters import rest_framework as filters
from app.filters import FlightFilter


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FlightFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ReadFlightSerializer
        else:
            return super(FlightViewSet, self).get_serializer_class()


class ReportView(views.APIView):

    def get(self, request, format=None):
        time_from = request.query_params.get('departure_time_from')
        time_to = request.query_params.get('arrival_time_to')
        qs = Airport.objects.all()
        if time_from:
            qs = qs.filter(flights_departure__departure_time__gte=time_from)
        if time_to:
            qs = qs.filter(flights_departure__arrival_time__lte=time_to)
        qs = qs.annotate(flight_count=Count('flights_departure__id'), inflight_avg=Avg('flights_departure__inflight_time'))
        qs = qs.filter(flight_count__gt=0)
        return Response(ReportSerializer(qs, many=True).data)
