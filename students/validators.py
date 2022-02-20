
from django.core.exceptions import ValidationError


def unique_number(phone_number):
    from .models import Students
    if Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('Phone number already exist')
