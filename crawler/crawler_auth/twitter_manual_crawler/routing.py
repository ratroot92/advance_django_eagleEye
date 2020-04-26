# chat/routing.py
from django.urls import re_path

from .consumers import Twitter_Tweets_Targets_Channels
from .consumers import Count_Tweets

websocket_urlpatterns = [
    # re_path(r're_scan/(?P<_username>\w+)/$', Twitter_Tweets_Targets_Channels),
    re_path(r're_scan/', Twitter_Tweets_Targets_Channels),
    re_path(r'tweets_db_insertion/', Count_Tweets),

]