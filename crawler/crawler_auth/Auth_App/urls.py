from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Auth_App'
urlpatterns = [
    path('', views.Login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('twitterTrendsByCountry/',views.twitterTrendsByCountry,name='twitterTrendsByCountry'),
    path('twitterTrendsWorldWide/',views.twitterTrendsWorldWide,name='twitterTrendsWorldWide'),
]
