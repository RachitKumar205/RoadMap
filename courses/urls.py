from django.urls import path
from .views import VideoAPIView, CreateRoadMapAPIView, GetUserRoadmapsAPIView, GetRoadMapAPIView, CreateRoadMapWithListAPIView

urlpatterns = [
    path('video/', VideoAPIView.as_view(), name="video"),
    path('create-roadmap/', CreateRoadMapAPIView.as_view(), name="create roadmap"),
    path('get-user-roadmaps/', GetUserRoadmapsAPIView.as_view(), name="get user roadmaps"),
    path('get-roadmap/', GetRoadMapAPIView.as_view(), name="get roadmap"),
    path('create-roadmap-list/', CreateRoadMapWithListAPIView.as_view(), name="create roadmap list")
]