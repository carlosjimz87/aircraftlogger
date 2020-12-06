from rest_framework import serializers
from app.models import Aircraft, Flight


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        exclude = ['id']

class FlightSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer()

    class Meta:
        model = Flight
        exclude = ['id']
