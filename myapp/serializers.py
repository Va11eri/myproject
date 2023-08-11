from rest_framework import serializers
from .models import User, Coords, Image, PerevalAdded

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['id', 'latitude', 'longitude', 'height']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'data', 'title']

class PerevalAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['id', 'beautyTitle', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'winter_level', 'summer_level', 'autumn_level', 'spring_level', 'images', 'status']