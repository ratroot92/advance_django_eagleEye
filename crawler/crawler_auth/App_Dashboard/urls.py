from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('dashboard/', views.App_Dashboard.as_view(),name='app_dashboard'),
     path('/addfacebooktarget/', views.addfacebooktarget,name='addfacebooktarget'),
   
    
]
