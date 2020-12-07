from rest_framework import viewsets
from app.models import Aircraft, Flight, Airport
from app.serializers import AircraftSerializer, FlightSerializer, ReadFlightSerializer, AirportSerializer


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ReadFlightSerializer
        else:
            return super(FlightViewSet, self).get_serializer_class()
