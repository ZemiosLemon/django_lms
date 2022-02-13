from django.db import models
from faker import Faker
from .validators import unique_number


class Teachers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone_number = models.CharField(
        max_length=20,
        validators=[unique_number]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}  age: {self.age} phone number: {self.phone_number}'

    @staticmethod
    def gen_teachers(count):
        fake = Faker()
        for _ in range(count):
            teach = Teachers(first_name=fake.first_name(),
                             last_name=fake.last_name(), age=fake.pyint(25, 75))
            teach.save()
