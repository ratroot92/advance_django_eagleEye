# chat/routing.py
from django.urls import re_path
from .consumers import Top_Trends

websocket_urlpatterns = [
    # routes defined in tweets_targets.html
    # re_path(r're_scan/(?P<_username>\w+)/$', Twitter_Tweets_Targets_Channels),
    re_path(r'topTrends/', Top_Trends),
   
]