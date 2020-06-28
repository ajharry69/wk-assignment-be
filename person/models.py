from django.db import models

from .utils import enums


class Person(models.Model):
    __GENDER_CHOICES = [(v.name, v.name) for _, v in enums.Gender.__members__.items()]
    name = models.CharField(max_length=150, )
    gender = models.CharField(max_length=10, choices=__GENDER_CHOICES, null=False, blank=False, )
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, default=None, )


class Location(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    altitude = models.FloatField(default=0)
    name = models.CharField(null=True, blank=True, default=None, max_length=150, )
