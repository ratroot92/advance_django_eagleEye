from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    #tweets_targets_urls
    path('/tweets_targets/',views.tweets_targets,name='tweets_targets'),
    path('/viewTweets/?P(?P<username>[0-9]+)\\/$/',views.viewTweets,name='viewTweets'),
    path('/delete_tweets_targets/?P(?P<username>[0-9]+)\\/$/',views.delete_tweets_targets,name='delete_tweets_targets'),
    path('/savetweets/',views.savetweets,name='gettweets'),

    #profiles_targets_urls
    path('/profiles_targets/',views.profiles_targets,name='profiles_targets'),
    path('/delete_profiles_targets/?P(?P<username>[0-9]+)\\/$/',views.delete_profiles_targets,name='delete_profiles_targets'),

]