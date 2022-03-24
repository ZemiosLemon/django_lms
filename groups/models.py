import datetime
import random

from django.db import models


class Group(models.Model):
    name_group = models.CharField(max_length=30)
    size_group = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateTimeField(null=True, blank=True)

    create_datime = models.DateTimeField(auto_now_add=True)
    update_datime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_group}'

    @staticmethod
    def gen_group(count):
        list_group = ['AA', 'AB', 'AC', 'AD', 'BA', 'BB', 'BC', 'BD']
        for _ in range(count):
            group = Group(name_group=random.choice(list_group) + "-" + str(random.randint(1, 6)),
                          size_group=random.randint(25, 40))
            group.save()
