from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth  import authenticate,login as authorize,logout as deauth
from bs4 import BeautifulSoup
import requests
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import models
from django_countries.fields import CountryField



def login(request):
       form = AuthenticationForm()
       if(request.method == 'POST'):
           form = AuthenticationForm()
           username=request.POST['username']
           password=request.POST['password']
           user =authenticate(username=username,password=password);
           if user is None:
                messages.add_message(request,messages.INFO,'Username or  Password is not valid ')
                return redirect('/login')
           else:
               authorize(request,user)
               return redirect('/home')
           
       else:
           if(request.user.is_authenticated):
               return redirect('/home')
           form = AuthenticationForm()
           
       return render(request, 'auth/login.html', {'title': 'Login', 'form': form})


def register(request):
       form = UserCreationForm()
       if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'User successfully registered')
                return redirect('/login')
       return render(request, 'auth/register.html', {'title': 'Registration', 'form': form})


def home(request):
    if(request.user.is_authenticated):
        trends=twitterTrends()
        return render(request,'home.html',{'trends':trends})
    return redirect('/login')

def logout(request):
      if(request.user.is_authenticated):
          
        deauth(request)
        messages.add_message(request,messages.SUCCESS,'User has been successfully logged out  ')
      else:
          messages.add_message(request,messages.INFO,'Login first')
      return redirect('/login')
          
          
          
          
def twitterTrends():
    url='https://trends24.in/pakistan/';
    page = requests.get(url);
    status_code=page.status_code;
    dic={};
    hashtag_name=[];
    hashtag_href=[];
    hashtag_count=[];
    if(status_code==200):
        data=BeautifulSoup(page.text,'lxml')
        new=data.find('ol',class_="trend-card__list");
        li=data.find_all('li')
        for i in li:
            hashtag_name.append(i.a.text)
            hashtag_href.append(i.a.attrs['href'])
            if(i.find('span')):
                hashtag_count.append(i.span.text)
            else:
                hashtag_count.append("count unavalible")
        
          
            
    dic = []
    for item in zip(hashtag_name, hashtag_count, hashtag_href):
    
        dic.append({
            'name':item[0],
            'count':item[1],
            'href':item[2]})
        
    return dic

def twitterTrendsByCountry(request):
    country=request.GET['country'];
    url='https://trends24.in/'+country;
    page = requests.get(url);
    status_code=page.status_code;
    dic={};
    hashtag_name=[];
    hashtag_href=[];
    hashtag_count=[];
    if(status_code==200):
        data=BeautifulSoup(page.text,'lxml')
        new=data.find('ol',class_="trend-card__list");
        li=data.find_all('li')
        for i in li:
            hashtag_name.append(i.a.text)
            hashtag_href.append(i.a.attrs['href'])
            if(i.find('span')):
                hashtag_count.append(i.span.text)
            else:
                hashtag_count.append("count unavalible")
        
          
   
    dic = []
    for i in range(len(hashtag_name)):
                 dic.append({i:
                {"name":hashtag_name[i],
                "count":hashtag_count[i],
                "href":hashtag_href[i]
                }})
    # for item in zip(hashtag_name, hashtag_count, hashtag_href):
    
    #     dic.append({
    #         'name':item[0],
    #         'count':item[1],
    #         'href':item[2]})
        
    # res = json.dumps(dic)
    # return HttpResponse(res,mimetype="application/json")
    return HttpResponse(dic)

 