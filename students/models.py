from django.db import models
from faker import Faker

from core.validators import unique_number


class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone_number = models.CharField(
        max_length=20,
        validators=[unique_number],
        default='1234567'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.age} {self.phone_number}'

    @staticmethod
    def gen_students(count):
        fake = Faker()
        for _ in range(count):
            stud = Students(first_name=fake.first_name(),
                            last_name=fake.last_name(), age=fake.pyint(15, 75))
            stud.save()
