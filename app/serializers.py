from rest_framework import serializers
from app.models import Aircraft, Flight


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class ReadFlightSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer(read_only=True)

    class Meta:
        model = Flight
        exclude = ['id']

    def create(self, validated_data):
        print("RVD:", validated_data)
        return super().create(validated_data)


class WriteFlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        exclude = ['id']

    def create(self, validated_data):
        print("WVD:", validated_data)
        return super().create(validated_data)
