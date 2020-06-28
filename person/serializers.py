from rest_framework import serializers

from . import models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('latitude', 'longitude', 'altitude', 'name',)


class PersonSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField(read_only=True, )
    photo = serializers.ImageField(write_only=True, )
    location = LocationSerializer(allow_null=True, )

    class Meta:
        model = models.Person
        fields = ('id', 'name', 'gender', 'photo', 'photo_url', 'location',)

    def create(self, validated_data):
        location = validated_data.pop('location') if 'location' in validated_data else None
        person = super().create(validated_data)
        if location:
            location_serializer = LocationSerializer(data=location)
            if location_serializer.is_valid():
                location_serializer.save(person=person)
        return person

    def get_photo_url(self, person):
        return self.context.get('request').build_absolute_uri(person.photo.url)
