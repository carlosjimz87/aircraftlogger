from rest_framework import serializers
from app.models import Aircraft, Flight


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer(read_only=True)

    class Meta:
        model = Flight
        exclude = ['id']
