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
    path('/addTwitterTarget/',views.addTwitterTarget,name='addTwitterTarget'),
    path('/addTwitterTarget/profile/',views.addTwitterTarget_Profile,name='addTwitterTarget_Profile'),
    path('/viewTweets/?P(?P<username>[0-9]+)\\/$/',views.viewTweets,name='viewTweets'),
    # path('<str:_username>/', views.username, name='username'),
    path('/generatePDF/?P(?P<username>[0-9]+)\\/$/',views.generatePDF,name='generatePDF'),
]	