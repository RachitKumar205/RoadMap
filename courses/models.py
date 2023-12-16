from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)

class RoadMap(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video)




