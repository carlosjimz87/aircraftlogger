from rest_framework import serializers, viewsets
from app.models import Aircraft, Flight
from app.serializers import AircraftSerializer, ReadFlightSerializer, WriteFlightSerializer
from rest_framework.response import Response
from rest_framework import status


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = WriteFlightSerializer

    def get_serializer_class(self):
        print("SA:", self.action)
        if self.action == 'list' or self.action == 'retrieve':
            return ReadFlightSerializer
        else:
            return WriteFlightSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
