from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth  import authenticate,login as authorize,logout as deauth
from bs4 import BeautifulSoup
import requests
import json
import twint
import nest_asyncio
from django.http import JsonResponse
from django.http import HttpResponse
from django.db import models
# from django_countries.fields import CountryField
import subprocess 
import asyncio


def Login(request):
       form = AuthenticationForm()
       if(request.method == 'POST'):
           form = AuthenticationForm()
           username=request.POST['username']
           password=request.POST['password']
           user =authenticate(username=username,password=password);
           if user is None:
                messages.add_message(request,messages.INFO,'Username or  Password is not valid ')
                return redirect('/')
           else:
               authorize(request,user)
               return redirect('/app/dashboard')
           
       else:
           if(request.user.is_authenticated):
               return redirect('/app/dashboard')
           form = AuthenticationForm()
           
       return render(request, 'Auth_App/Login.html', {'title': 'Login', 'form': form})


def register(request):
       form = UserCreationForm()
       if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'User successfully registered')
                return redirect('/')
       return render(request, 'auth/register.html', {'title': 'Registration', 'form': form})


def home(request):
    if(request.user.is_authenticated):
        trends=twitterTrends()
        world_trends=twitterTrendsWorldwide()
        return render(request,'home.html',{'trends':trends,'world_trends':world_trends})
    return redirect('/')

def logout(request):
      if(request.user.is_authenticated):
          
        deauth(request)
        messages.add_message(request,messages.SUCCESS,'User has been successfully logged out  ')
      else:
          messages.add_message(request,messages.INFO,'Login first')
      return redirect('/')
          
          
          
          
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
                 dic.append(
                {"name":hashtag_name[i],
                "count":hashtag_count[i],
                "href":hashtag_href[i]
                })
    
    return JsonResponse(dic,safe=False)

def  twitterTrendsWorldWide(request):
    url='https://trends24.in/';
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
                 dic.append(
                {"name":hashtag_name[i],
                "count":hashtag_count[i],
                "href":hashtag_href[i]
                })
    
    return JsonResponse(dic,safe=False)

#Twitter Index
   
 