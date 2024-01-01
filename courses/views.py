from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import VideoSerializer, RoadMapSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Video, RoadMap
from pytube import Playlist, YouTube
import pytube
from django.forms.models import model_to_dict
from rest_framework import parsers, status


# Create your views here.

class VideoAPIView(APIView):

    def post(self, request):
        serializer = VideoSerializer(request)
        if serializer.is_valid:
            serializer.save()


class GetUserRoadmapsAPIView(APIView):

    def post(self, request):
        token = request.data.get("token")
        token = Token.objects.filter(key=token).first()

        if token:
            user = token.user
            roadmaps = RoadMap.objects.filter(user=user)
            roadmap_data = []

            for roadmap in roadmaps:
                roadmap_dict = model_to_dict(roadmap)
                roadmap_dict["videos"] = [{"id": vid.pk, "title": vid.name, "thumbnail": vid.thumbnail, "url": vid.url}
                                          for vid in roadmap.videos.all()]
                roadmap_data.append(roadmap_dict)

            return JsonResponse({"roadmaps": roadmap_data})


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


class GetRoadMapAPIView(APIView):

    def post(self, request):
        id = request.data.get("id")
        roadmap = RoadMap.objects.get(id=id)
        roadmap_data = []
        roadmap_dict = model_to_dict(roadmap)
        roadmap_dict["videos"] = [{"id": vid.pk, "title": vid.name, "thumbnail": vid.thumbnail, "url": vid.url}
                                  for vid in roadmap.videos.all()]
        roadmap_data.append(roadmap_dict)
        return JsonResponse({"roadmap": roadmap_data})

class CreateRoadMapWithListAPIView(APIView):
    parser_classes = (parsers.JSONParser,)

    def post(self, request):
        try:
            data = request.data
            name = data["name"]
            email = data["email"]
            urls = data.get("urls", [])

            if not urls:
                return JsonResponse({"error": "Missing 'urls' list in request data."}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(email=email)
            roadmap = RoadMap(name=name, user=user)
            roadmap.save()

            for url in urls:
                v = YouTube(url)
                vid, created = Video.objects.get_or_create(url=url, name=v.title, thumbnail=v.thumbnail_url)
                roadmap.videos.add(vid)

            return JsonResponse({"message": "successfully saved playlist"})
        except KeyError as e:
            return JsonResponse({"error": f"Missing required field: {e}"}, status=status.HTTP_400_BAD_REQUEST)







