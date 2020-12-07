from django.utils.timezone import now
from django.core.exceptions import ValidationError


def departure_time_validator(value):
    if value < now():
        raise ValidationError(
            '%(value) is an invalid date. Must be a future datetime.', params={'value': value})


def arrival_time_validator(obj):
    if obj.arrival_time < obj.departure_time:
        raise ValidationError(
            '%(value) is an invalid date. Must be after the departure.', params={'value': obj.arrival})
