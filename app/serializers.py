from rest_framework import serializers
from app.models import Aircraft, Flight, Airport


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        exclude = ['id']


class ReadFlightSerializer(FlightSerializer):
    aircraft = AircraftSerializer()
    departure = AirportSerializer()
    arrival = AirportSerializer()
