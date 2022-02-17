from django.db import models
from faker import Faker


class Teachers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.age}'

    @staticmethod
    def gen_teachers(count):
        fake = Faker()
        for _ in range(count):
            teach = Teachers(first_name=fake.first_name(),
                             last_name=fake.last_name(), age=fake.pyint(25, 75))
            teach.save()
