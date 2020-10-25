from django.shortcuts import render
from django.views.generic import TemplateView,View
from Data_Acquisition_App.Trends_24 import Twitter_Trends

"""initalize Class objects """

# Create your views here.
class App_Dashboard(View):
    """ returns application main dashbaord """
    def get(self,request,*args,**kwargs):
        Get_Trends= Twitter_Trends()
        Top_World_Trends=Get_Trends.World_Top_Trends()
        Pakistan_Top_Trends=Get_Trends.Pakistan_Top_Trends()
        return render(request,'App_Dashboard/App_Dashboard.html',{'Top_World_Trends':Top_World_Trends,'Pakistan_Top_Trends':Pakistan_Top_Trends})

def addfacebooktarget(request):
    return render(request,'App_Dashboard/addtargets/facebook_target.html')