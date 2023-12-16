from django.urls import path
from .views import VideoAPIView, CreateRoadMapAPIView, GetVideoAPIView

urlpatterns = [
    path('video/', VideoAPIView.as_view(), name="video"),
    path('create-roadmap/', CreateRoadMapAPIView.as_view(), name="roadmap"),
    path('get-videos/', GetVideoAPIView.as_view(), name="get videos")
]