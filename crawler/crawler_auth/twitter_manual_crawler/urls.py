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
    path('/viewProfile/following_locations/?P(?P<username>[0-9]+)\\/$/',views.viewProfile_Following_locations,name='viewProfile_Following_locations'),
    path('/viewProfile/followers_locations/?P(?P<username>[0-9]+)\\/$/',views.viewProfile_Followers_locations,name='viewProfile_Followers_locations'),
    path('/viewProfile/followers_tree/?P(?P<username>[0-9]+)\\/$/',views.viewProfile_Followers_tree,name='viewProfile_Followers_tree'),
    path('/viewProfile/following_tree/?P(?P<username>[0-9]+)\\/$/',views.viewProfile_Following_tree,name='viewProfile_Following_tree'),
    path('/viewProfile/full_profile/?P(?P<username>[0-9]+)\\/$/',views.viewProfile_Full_profile,name='viewProfile_Full_profile'),
    path('/test_notifications/',views.test_notifications,name='test_notifications'),
    # logs
    path('/logs/',views.logs,name='logs'),
    # geo targets
    path('/geo_targets/',views.geo_targets,name='geo_targets'),
    path('/bbox/',views.bbox,name='bbox'),
    path('/rapid_search/',views.rapid_search,name='rapid_search')

]