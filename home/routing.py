from django.urls import path
from .consumers import AccidentAlertConsumer

websocket_urlpatterns = [
    path('ws/alerts/', AccidentAlertConsumer.as_asgi()),
]
