from django.urls import path
from . import views

urlpatterns = [
    path('process_video/', views.process_video, name='process_video'),
    path("traffic/",views.traffic_cam , name = "traffic_cam"),
    path('process_accident/',views.process_video_accident , name="process_accident"),
    path("accident/",views.accident_page , name="accident_page"),
]
