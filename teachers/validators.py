
from django.core.exceptions import ValidationError


def unique_number(phone_number):
    from .models import Teachers
    if Teachers.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(f'The phone number {phone_number} is already in use')
