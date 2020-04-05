from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'dashboard/index.html');

def addfacebooktarget(request):
    return render(request,'dashboard/addtargets/facebook_target.html')