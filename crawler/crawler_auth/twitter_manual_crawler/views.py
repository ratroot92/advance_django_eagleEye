
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as authorize, logout as deauth
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse
import twint
import nest_asyncio
import asyncio
from .models import Users,Tweets
import djongo
import json

# task imports
from .tasks import getTweets
from .tasks import getAllFollowers
from .tasks import getSingleUser

# model imports
from .models import tweets_target_model
from .models import tweets_target_form
from .models import profiles_target_form
from .models import profiles_target_model
from .models import  Followers
def gettweets(request,_username):
    Tweets.objects.filter(username=_username)
    return render (request,'tweets.html')




def tweets_targets(request):
     form=tweets_target_form
     tweets_targets=tweets_target_model.objects.all()
     if request.method ==  'POST':
         form=tweets_target_form(request.POST or None)
         if form.is_valid():
             form.save()
            #  r=asd.delay(request.POST['twitter_username'])
             messages.success(request,'Tweets Target added successfully')
             print("form saved success")
             r=getTweets.delay(request.POST['twitter_username'])
             return redirect('/tw/tweets_targets')
         else:
             print("tweets target form not saved : error ")
             messages.error(request,'Tweets Target insertion Failed')
     return render(request,'tweets_targets.html',{'form':form,'tweets_targets':tweets_targets})











def viewTweets(request,username):
    lower_username=username.lower()
    print(lower_username)
    tweets_list=Tweets.objects.filter(username=lower_username).order_by('-datestamp')
    length=len(tweets_list)
    print(length)
    print(type(length))
    if(len(tweets_list)<=0):
         messages.error(request,'No tweets found ')
         return redirect('/tw/tweets_targets')
    l=(len(tweets_list)//2)
    paginator=Paginator(tweets_list,l)
    page=request.GET.get('page')
    try:
        tweets=paginator.page(page)
    except PageNotAnInteger:
        tweets=paginator.page(1)
    except EmptyPage:
        tweets=paginator.page(paginator.num_pages)
    return render(request,'view_tweets.html',{'tweets':tweets})


def delete_tweets_targets(request,username):
         lower_username=username.lower()
         tweets_target_model.objects.filter(twitter_username=username).all().delete()
         Tweets.objects.filter(username=lower_username).all().delete()
         messages.success(request,'Tweets Target deleted successfully')
         return redirect('/tw/tweets_targets')






#profiles _targets_views
def profiles_targets(request):
    form=profiles_target_form
    profiles_targets=profiles_target_model.objects.all()
    if request.method ==  'POST':
        form=profiles_target_form(request.POST or None)
        if form.is_valid():
            form.save()
            s=getSingleUser.delay(request.POST['twitter_username'])
            r=getAllFollowers.delay(request.POST['twitter_username'])
            messages.success(request,'Profile Target added successfully')
            # r=getTweets.delay(request.POST['twitter_username'])
            return redirect('/tw/profiles_targets')
        else:
                print("Profile Target Insertion Failed  : error ")
                messages.error(request,'profiles Target insertion Failed')
    return render(request,'profiles_targets.html',{'form':form,'profiles_targets':profiles_targets})



def delete_profiles_targets(request,username):
         ower_username=username.lower()
         deleted_target=profiles_target_model.objects.get(twitter_username=username)
         Followers.objects.filter(following_id_fk=deleted_target.followers_fkey).all().delete()
         profiles_target_model.objects.get(twitter_username=username).delete()
         messages.success(request,'Profile Target deleted successfully')
         return redirect('/tw/profiles_targets')















def index(request):
    user_dict=getUser()
    new_user=Users(id=user_dict['id'],
          id_str=user_dict['id_str'],
          name=user_dict['name'],
          username=user_dict['username'],
          bio=user_dict['bio'],
          location=user_dict['location'],
          url=user_dict['url'],
          join_date=user_dict['join_date'],
          join_time=user_dict['join_time'],
          tweets=user_dict['tweets'],
          following=user_dict['following'],
          followers=user_dict['followers'],
          likes=user_dict['likes'],
          media=user_dict['media'],
          private=user_dict['is_private'],
          verified=user_dict['is_verified'],
          profile_image_url=user_dict['profile_image_url'],
          background_image=user_dict['background_image'],

          )
    new_user.save()

    return render(request,'userprofile.html')

def savetweets(request):
    for  i in range(20):
        status=Tweets(**{
        "id" : '1192734890116206593',
        "id_str" : "1192734890116206593",
        "conversation_id" : "1192539563203473413",
        "datetime" : "1573205132000",
        "datestamp" : "2019-11-08",
        "timestamp" : "14:25:32",
        "user_id" : "871226174550286336",
        "user_id_str" : "871226174550286336",
        "username" : "maliksblr92",
        "name" : "AwaRa.....",
        "place" : "",
        "timezone" : "PKT",
        "mentions" : "['surkhminahil']",
        "urls" : "[]",
        "photos" : "[]",
        "video" : "0",
        "text" : "Get a life grl",
        "hashtags" : "[]",
        "cashtags" : "[]",
        "replies_count" : "0",
        "likes_count" : "0",
        "retweets_count" : "0",
        "link" : "https://twitter.com/maliksblr92/status/1192734890116206593",
        "user_rt_id" : "",
        "retweet" : "False",
        "retweet_id" : "",
        "retweet_date" : "",
        "quote_url" : "",
            "near" : "",
        "geo" : "",
        "source" : "",
        "reply_to" : "[{'user_id': '871226174550286336', 'username': 'maliksblr92'}, {'user_id': '803581791168765952', 'username': 'surkhminahil'}]"
})
        status.save()
        print(status)
    return render(request,'userprofile.html')

























# get profile data
def getUser():
    # nest_asyncio.apply()
    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    c.Username = "maliksblr92"
    c.Store_object = True
    user = {'id': ''}
    twint.run.Lookup(c)
    u = twint.output.users_list
    print(u)
    user['id'] = format(u[0].id)
    user['id_str'] = format(u[0].id)
    user['name'] = u[0].name
    user['username'] = u[0].username
    user['bio'] = u[0].bio
    user['location'] = u[0].location
    user['url'] = u[0].location
    user['join_date'] = u[0].join_date
    user['join_time'] = u[0].join_time
    user['tweets'] = u[0].tweets
    user['following'] = u[0].following
    user['followers'] = u[0].followers
    user['likes'] = u[0].likes
    user['media'] = u[0].media_count
    user['is_private'] = u[0].is_private
    user['is_verified'] = u[0].is_verified
    user['profile_image_url'] = u[0].avatar
    user['background_image'] = u[0].background_image


    return(user)
