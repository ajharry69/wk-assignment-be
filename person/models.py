from django.conf import settings
from django.db import models
from geopy.geocoders import GoogleV3

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
    address = models.CharField(null=True, blank=True, default=None, max_length=150, )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # geolocator = GoogleV3(api_key=settings.GOOGLE_MAPS_API_KEY, )
        # location = geolocator.reverse(f'{self.latitude},{self.longitude}')
        # self.address = location.address
        super().save(force_insert, force_update, using, update_fields)
