# chat/routing.py
from django.urls import re_path

from .consumer import TwtterConsumer,TweetCount,ProfileScan

websocket_urlpatterns = [
    re_path(r'scan/(?P<_username>\w+)/$', TwtterConsumer),
    re_path(r'getCount/', TweetCount),
    re_path(r'twitter/profile_scan/',ProfileScan)
    
]