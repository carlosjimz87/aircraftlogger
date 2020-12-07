from rest_framework import serializers
from app.models import Aircraft, Flight, Airport
from app.validators import arrival_time_validator,departure_time_validator


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

    def validate(self, attrs):
        departure_time_validator(attrs)
        arrival_time_validator(attrs)
        return attrs


class ReadFlightSerializer(FlightSerializer):
    aircraft = AircraftSerializer()
    departure = AirportSerializer()
    arrival = AirportSerializer()
