from django.shortcuts import render
from django.views.generic import TemplateView,View
# Create your views here.
class App_Dashboard(View):
    """ returns application main dashbaord """
    def get(self,request,*args,**kwargs):
        return render(request,'App_Dashboard/App_Dashboard.html')

def addfacebooktarget(request):
    return render(request,'App_Dashboard/addtargets/facebook_target.html')