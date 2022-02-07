from django.db import models


class Group(models.Model):
    name_group = models.CharField(max_length=30)
    size_group = models.IntegerField()
