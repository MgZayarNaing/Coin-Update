# myapp/routing.py

from django.urls import re_path
from .consumers import CountdownConsumer

websocket_urlpatterns = [
    re_path(r'ws/countdown/$', CountdownConsumer.as_asgi()),
]
