from django.utils.timezone import now
from rest_framework.serializers import ValidationError


def departure_time_validator(fields):
    if fields['departure_time'] < now():
        raise ValidationError({"departure_time": "must be a future datetime"})


def arrival_time_validator(fields):
    if fields["arrival_time"] < fields["departure_time"]:
        raise ValidationError(
            {"arrival_time": "must be a after departure time"})
