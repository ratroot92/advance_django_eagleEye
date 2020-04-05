from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
    #twitter engine urls 
    path('index/',views.twitterIndex,name='twitterIndex'),
    path('/submitTarget/',views.submitTarget,name='submitTarget'),
    path('tweets_keyword/',views.tweets_keyword,name='tweets_keyword'),
    path('fullProfile/',views.fullProfile,name='fullProfile'),
    path('getFollowersList/',views.getFollowersList,name='getFollowersList'),
    path('getFollowingList/',views.getFollowingList,name='getFollowingList'),
]	