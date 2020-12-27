from django.shortcuts import render
from django.views.generic import TemplateView,View
from Data_Acquisition_App.Trends_24 import Twitter_Trends
from Data_Acquisition_App.Mongo_Models import *
"""initalize Class objects """
# Create your views here.
class App_Dashboard(View):
    """ returns application main dashbaord """
    def get(self,request,*args,**kwargs):
        topWorldTrends=Top_World_Trends.objects.first()
        topPakistanTrends=Countries_Top_Trends_Document.objects.filter(country_name="pakistan")
        return render(request,'App_Dashboard/App_Dashboard.html',{'Top_World_Trends':topWorldTrends,'Pakistan_Top_Trends':topPakistanTrends[0]})

def addfacebooktarget(request):
    return render(request,'App_Dashboard/addtargets/facebook_target.html')