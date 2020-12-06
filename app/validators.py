from django.utils.timezone import now
from django.core.exceptions import ValidationError


def departure_time_validator(value):
    if value < now():
        raise ValidationError(
            '%(value) is an invalid date. Must be a future datetime.', params={'value': value})
