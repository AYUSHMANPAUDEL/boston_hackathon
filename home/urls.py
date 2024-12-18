from django.urls import path
from . import views

urlpatterns = [
    path('process_video/', views.process_video, name='process_video'),
    path("traffic/",views.traffic_cam , name = "traffic_cam"),
    path('process_accident/',views.process_video_accident , name="process_accident"),
    path("accident/",views.accident_page , name="accident_page"),
    path("",views.main_page , name="main_page"),  
    path('projects/', views.projects, name='projects'),
    path('analytics/', views.analytics, name='analytics'),
    path("police/",views.police_page , name="police_page"),

    path('police_stations/', views.police_stations_police, name='police_stations_police'),
    path('officers/', views.officers_police, name='officers_police'),
    path('reports/', views.reports_police, name='reports_police'),
    path('live_alerts/', views.live_alerts_police, name='live_alerts_police'),

    path("firedepartment/",views.firedepart_page , name="fire_page"),
       path('live-alerts_firedep/', views.live_alerts_firedep, name='live_alerts_firedep'),





     path("ambulance/",views.ambulance_page , name="ambulance_page"),
      path('live_alerts_ambulance/', views.live_alerts_ambulance, name='live_alerts_ambulance'),

]
