# chat/routing.py
from django.urls import re_path

from .consumers import Twitter_Tweets_Targets_Channels
from .consumers import CELERY_NOTIFICATIONS_TWITTER_MANUAl_CRAWLER
from .consumers import Rescan_Twitter_Profile_Target
from .consumers import TweetCount
websocket_urlpatterns = [
    # routes defined in tweets_targets.html
    # re_path(r're_scan/(?P<_username>\w+)/$', Twitter_Tweets_Targets_Channels),
    re_path(r're_scan/', Twitter_Tweets_Targets_Channels),
    re_path(r'celery_notifications/twitter_manual_crawler/',CELERY_NOTIFICATIONS_TWITTER_MANUAl_CRAWLER),
    # routes defined in profiles_targets.html
    re_path(r'getCount/', TweetCount),
    re_path(r'rescan/profile_targets/',Rescan_Twitter_Profile_Target)
]