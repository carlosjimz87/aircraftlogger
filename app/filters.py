from django_filters import rest_framework as filters
from app.models import Flight


class FlightFilter(filters.FilterSet):
    """
    Adds a syntax for request params to filter :model:`app.Flight`s using `departure_time` and `arrival_time`.
    """
    departure_time_from = filters.DateTimeFilter(field_name="departure_time", lookup_expr='gte')
    arrival_time_to = filters.DateTimeFilter(field_name="arrival_time", lookup_expr='lte')

    class Meta:
        model = Flight
        fields = ['arrival', 'departure', 'departure_time_from', 'arrival_time_to']

