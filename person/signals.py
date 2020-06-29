from django.conf import settings
from django.db.models.signals import post_save
from geopy.geocoders import GoogleV3

from .models import Location


async def on_location_post_save(sender, instance, created, **kwargs):
    """
    retrieve and update geographical coordinates on created
    """
    async with (GoogleV3(api_key=settings.GOOGLE_MAPS_API_KEY, )) as geolocator:
        location = await geolocator.reverse(f'{instance.latitude},{instance.longitude}')
        instance.address = location.address
        instance.save()


# post_save.connect(on_location_post_save, Location, dispatch_uid='location01')
