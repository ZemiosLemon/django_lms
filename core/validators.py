import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def unique_number(phone_number):
    from students.models import Students
    if Students.objects.filter(phone_number=phone_number).exists():
        raise ValidationError('Phone number already exist')


@deconstructible
class AdultValidator:
    def __init__(self, age_limit):
        self.age_limit = age_limit

    def __call__(self, *args, **kwargs):
        age = datetime.date.today().year - args[0].year
        if age < self.age_limit:
            raise ValidationError(f'Age should be greater than {self.age_limit} y.o.')

    def __eq__(self, other):
        return (
                isinstance(other, self.__class__) and
                self.age_limit == other.age_limit
        )
