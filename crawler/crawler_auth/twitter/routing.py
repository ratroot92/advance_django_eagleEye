# chat/routing.py
from django.urls import re_path

from .consumer import TwtterConsumer

websocket_urlpatterns = [
    re_path(r'scan/(?P<_username>\w+)/$', TwtterConsumer),
    
]