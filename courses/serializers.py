from rest_framework import serializers
from .models import Video, RoadMap

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class RoadMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadMap
        fields = '__all__'
