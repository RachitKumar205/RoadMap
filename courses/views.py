from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import VideoSerializer, RoadMapSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Video, RoadMap
from pytube import Playlist, YouTube



# Create your views here.

class VideoAPIView(APIView):

    def post(self, request):
        serializer = VideoSerializer(request)
        if serializer.is_valid:
            serializer.save()

class GetVideoAPIView(APIView):

    def post(self, request):
        token = request.data.get("token")
        token = Token.objects.filter(key=token).first()


        if token:
            user = token.user
            vids = Video.objects.all()
            videos = [{"id":vid.pk, "title":vid.name, "thumbnail":vid.thumbnail} for vid in vids]

        return JsonResponse({"videos": videos})


class CreateRoadMapAPIView(APIView):

    def post(self, request):
        url = request.data.get("url")
        name = request.data.get("name")
        email = request.data.get("email")
        user = User.objects.get(email=email)
        roadmap = RoadMap(name=name, user=user)
        roadmap.save()
        p = Playlist(url)

        for i in p:
            v = YouTube(i)
            vid, created = Video.objects.get_or_create(url=i, name=v.title, thumbnail=v.thumbnail_url)
            roadmap.videos.add(vid)

        return JsonResponse({"message":"successfully saved playlist"})





