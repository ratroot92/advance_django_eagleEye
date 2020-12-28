
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
import json
from Data_Acquisition_App.Mongo_Models import *
from django.views.generic import TemplateView,View
# task imports
from .tasks import getTweets
from .tasks import getAllFollowers
from .tasks import getSingleUser
from .tasks import getAllFollowings

# model imports
from .models import tweets_target_model
from .models import tweets_target_form
from .models import profiles_target_form
from .models import profiles_target_model
from .models import  Followers,Followings
from .models import Activity_Logger
# geopy imports
import geopy
from geopy import Nominatim



from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .tasks import asd

""" """
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def gettweets(request,_username):
    Tweets.objects.filter(username=_username)
    return render (request,'tweets.html')




class Tweets_Targets(View):
    def get(self,request,*args,**kwargs):
         print(f"{bcolors.WARNING}Twitter Target -- GET  ,{bcolors.ENDC}")
         Obj=Twitter_Target_Document()
         tweets_targets=Obj.Get_All_Twitter_Targets()
         return render(request,'tweets_targets.html',{'PERIODIC_INTERVALS':PERIODIC_INTERVALS,'tweets_targets':tweets_targets})
    def post(self,request,*args,**kwargs):
        target_platform=request.POST.get('target_platform')
        target_type=request.POST.get('target_type')
        target_username=request.POST.get('target_username')
        target_scheduling=request.POST.get('target_scheduling')
        print(f"{bcolors.WARNING}Twitter Target -- POST ,{bcolors.ENDC}")
        print(f"{bcolors.WARNING}{target_platform},{target_type},{target_username},{target_scheduling},{bcolors.ENDC}")
        try:
            Obj=Twitter_Target_Document()
            targetExist=Obj.UserExist(target_username)
            if not targetExist:
                Query=Obj.Create_Twitter_Target(target_platform,target_type,target_username,target_scheduling)
                if(Query):
                    celery_task_sent=getTweets.delay(target_username)
                    messages.success(request, 'Target created successfully.')
                    return redirect('/tw/twitter')
                else:
                    messages.error(request, 'Operation failed .')
                  
                    return redirect('/tw/twitter')
            else:
                messages.error(request, 'Target already exist ')
                return redirect('/tw/twitter')
        except Exception as e:
            print(e)
            messages.error(request, 'Operation failed .')
            return redirect('/tw/twitter')
       
class Delete_Tweet_Target(View):
    def get(self,request,*args,**kwargs):
            print(f"{bcolors.WARNING}Delete_Tweet_Target -- GET  ,{bcolors.ENDC}")
            username=kwargs.get('username',None)
            try:
                targetExist=Twitter_Target_Document.objects.filter(target_username=username).first()
                if  targetExist:
                    targetExist.delete()
                    messages.success(request, 'Twitter Target Deleted Successfully   ')
                    return redirect('/tw/twitter')
                else:
                    messages.error(request, 'Failed to Delete Target  ')
                    return redirect('/tw/twitter')
            except Exception as e:
                print(e)
                messages.error(request, 'Operation failed .')
                return redirect('/tw/twitter')
        

    def post(self,request,*args,**kwargs):
        pass

def tweets_targets(request):
     form=tweets_target_form
     tweets_targets=[]
     if request.method ==  'POST':
         form=tweets_target_form(request.POST or None)
         if form.is_valid():
             form.save()
             messages.success(request,'Tweets Target added successfully')
             print("form saved success")
             r=getTweets.delay(request.POST['twitter_username'])
             return redirect('/tw/tweets_targets')
         else:
           
             print("tweets target form not saved : error ")
             messages.error(request,'Tweets Target insertion Failed')
     return render(request,'tweets_targets.html',{'form':form,'PERIODIC_INTERVALS':PERIODIC_INTERVALS,'tweets_targets':tweets_targets})







def viewTweetsJson(request,username):
    print(f"{bcolors.WARNING}Twitter_Crawler  -- viewTweetsJson(request,username)   ,{bcolors.ENDC}")
    lower_username=username.lower()
    targetExist=Twitter_Target_Document.objects.filter(target_username=lower_username).first()
    if(targetExist.tweets_count < 1):
        messages.error(request,'No tweets found ')
        return redirect('/tw/tweets_targets')
    else:       
        return render(request,'Tweets_Json_Viewer.html',{'tweets':targetExist.tweets})
        #return render(request,'Tweets_Json_Viewer.html',{'tweets':json.dumps(targetExist.tweets)})


def viewTweets(request,username):
    print(f"{bcolors.WARNING}Twitter_Crawler  -- viewTweets(request,username)   ,{bcolors.ENDC}")
    lower_username=username.lower()
    targetExist=Twitter_Target_Document.objects.filter(target_username=lower_username).first()
    if(targetExist.tweets_count < 1):
        messages.error(request,'No tweets found ')
        return redirect('/tw/tweets_targets')
    else:      
        l=(len(targetExist.tweets)//2)
        paginator=Paginator(targetExist.tweets,l)
        page=request.GET.get('page')
        try:
            tweets=paginator.page(page)
        except PageNotAnInteger:
            tweets=paginator.page(1)
        except EmptyPage:
            tweets=paginator.page(paginator.num_pages)
    return render(request,'view_tweets.html',{'tweets':tweets})
   
# def viewTweets(request,username):
#      print(f"{bcolors.WARNING}Twitter_Crawler  -- viewTweets(request,username)   ,{bcolors.ENDC}")
#     lower_username=username.lower()
#     tweets_list=Tweets.objects.filter(username=lower_username).order_by('-datestamp')
#     length=len(tweets_list)
#     print(length)
#     print(type(length))
#     if(len(tweets_list)<=0):
#          messages.error(request,'No tweets found ')
#          return redirect('/tw/tweets_targets')
#     l=(len(tweets_list)//2)
#     paginator=Paginator(tweets_list,l)
#     page=request.GET.get('page')
#     try:
#         tweets=paginator.page(page)
#     except PageNotAnInteger:
#         tweets=paginator.page(1)
#     except EmptyPage:
#         tweets=paginator.page(paginator.num_pages)
#     return render(request,'view_tweets.html',{'tweets':tweets})


def delete_tweets_targets(request,username):
         lower_username=username.lower()
         tweets_target_model.objects.filter(twitter_username=username).all().delete()
         Tweets.objects.filter(username=lower_username).all().delete()
         messages.success(request,' Twitter Tweets Target eleted successfully')
         log=Activity_Logger(activity_name='Deleting Tweets Target',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Tweets Target  With Username = '+username+' Deleted Successfully',
                             activity_status='successfull')
         log.save()
         return redirect('/tw/tweets_targets')






#profiles _targets_views
def profiles_targets(request):
    form=profiles_target_form
    profiles_targets=profiles_target_model.objects.all()
    if request.method ==  'POST':
        form=profiles_target_form(request.POST or None)
        if form.is_valid():
            form.save()
            log=Activity_Logger(activity_name='Adding Twitter Profile Target',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile  Target Added With Username = '+request.POST['twitter_username'],
                             activity_status='successfull')
            log.save()
            s=getSingleUser.delay(request.POST['twitter_username'])
            r=getAllFollowers.delay(request.POST['twitter_username'])
            t=getAllFollowings.delay(request.POST['twitter_username'])
            messages.success(request,'Profile Target added successfully')
            # r=getTweets.delay(request.POST['twitter_username'])
            return redirect('/tw/profiles_targets')
        else:
                print("Profile Target Insertion Failed  : error ")
                messages.error(request,'profiles Target insertion Failed')
                log=Activity_Logger(activity_name='Adding Twitter Profile Target',
                             activity_app='Twitter_Crawler',
                             activity_details='Failed to Add Twitter Profile Target With Username = '+request.POST['twitter_username'+'\n Target Already Exsist'],
                             activity_status='failure')
                log.save()
    return render(request,'profiles_targets.html',{'form':form,'profiles_targets':profiles_targets})



def delete_profiles_targets(request,username):
         lower_username=username.lower()
         deleted_target=profiles_target_model.objects.get(twitter_username=username)
         Followers.objects.filter(follower_id_fk=deleted_target.followers_fkey).all().delete()
         Followings.objects.filter(following_id_fk=deleted_target.followers_fkey).all().delete()
         profiles_target_model.objects.get(twitter_username=username).delete()
         messages.success(request,'Profile Target deleted successfully')
         log=Activity_Logger(activity_name='Deleting Twitter Profile Target',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile  Target  With Username = '+username+' Deleted Successfully',
                             activity_status='successfull')
         log.save()
         return redirect('/tw/profiles_targets')




def viewProfile_Following_locations(request,username):
     profile_target=profiles_target_model.objects.get(twitter_username=username)
     following_list=Followings.objects.filter(following_id_fk=profile_target.followers_fkey).order_by('-join_date')
     if(len(following_list)<1):
          messages.success(request,'Target Has no Followings ! Operation Failed  ')
          return redirect('/tw/profiles_targets')
     log=Activity_Logger(activity_name='Viewing Followings Locations',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile Target  With Username = '+username+' Followings Locations were Viewed',
                             activity_status='successfull')
     log.save()
     return render(request,'profile_targets_following_locations.html',{'following_list':following_list,'profile_target':profile_target})



def viewProfile_Followers_locations(request,username):
     profile_target=profiles_target_model.objects.get(twitter_username=username)
     followers_list=Followers.objects.filter(follower_id_fk=profile_target.followers_fkey).order_by('-join_date')
     if(len(followers_list)<1):
          messages.success(request,'Target Has no Followers ! Operation Failed  ')
          return redirect('/tw/profiles_targets')
     log=Activity_Logger(activity_name='Viewing Followers Locations',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile Target  With Username = '+username+' Followers Locations were Viewed',
                             activity_status='successfull')
     log.save()
     return render(request,'profile_targets_followers_locations.html',{'followers_list':followers_list,'profile_target':profile_target})

def viewProfile_Followers_tree(request,username):
    profile_target=profiles_target_model.objects.get(twitter_username=username)
    followers_list=Followers.objects.filter(follower_id_fk=profile_target.followers_fkey).order_by('-join_date')
    if(len(followers_list)<1):
          messages.success(request,'Target Has no Followers ! Operation Failed  ')
          return redirect('/tw/profiles_targets')
    log=Activity_Logger(activity_name='Viewing Followers Tree',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile Target  With Username = '+username+' Followers Tree was Viewed',
                             activity_status='successfull')
    log.save()
    return render(request,'profile_targets_followers_tree.html',{'followers_list':followers_list})


def viewProfile_Following_tree(request,username):
    profile_target=profiles_target_model.objects.get(twitter_username=username)
    following_list=Followings.objects.filter(following_id_fk=profile_target.followers_fkey).order_by('-join_date')
    if(len(following_list)<1):
          messages.success(request,'Target Has no Followings ! Operation Failed  ')
          return redirect('/tw/profiles_targets')
    log=Activity_Logger(activity_name='Viewing Followings Tree',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile Target  With Username = '+username+' Followings Tree was Viewed',
                             activity_status='successfull')
    log.save()
    return render(request,'profile_targets_following_tree.html',{'following_list':following_list,'profile_targets':profile_target})


def viewProfile_Full_profile(request,username):
    profile_target=profiles_target_model.objects.get(twitter_username=username)
    followers_list=Followers.objects.filter(follower_id_fk=profile_target.followers_fkey).order_by('-join_date')
    following_list=Followings.objects.filter(following_id_fk=profile_target.followers_fkey).order_by('-join_date')
    log=Activity_Logger(activity_name='Viewing Complete Profile',
                             activity_app='Twitter_Crawler',
                             activity_details='Twitter Profile Target  With Username = '+username+' Complete Profile was Viewed',
                             activity_status='successfull')
    log.save()
    return render(request,'profile_targets_full_profile.html',{'followers_list':followers_list,'following_list':following_list,'profile_target':profile_target})



def test_notifications(request):
    r=asd.delay()
    return HttpResponse('<div>asdasdasdasdadasda</div>')

def logs(request):
    all_logs=Activity_Logger.objects.all().order_by('-created_at')
    print(len(all_logs))
    return render(request,'logs.html',{'logs':all_logs})



# geo targets views


def geo_targets(request):
    return render(request,'geo_targets.html')

def bbox(request):
    return render(request,'bbox.html')

def rapid_search(request):
    if request.method=='POST':
        search_type=request.POST['search_type']



        if search_type=='phrase_seacrh':
            phrase=request.POST['phrase']
            tweet_type=request.POST['tweet_type']
            username=''
            print("######################################################")
            print("Search Type == ",search_type)
            print("Tweets Type == ",tweet_type)
            print("######################################################")
            limit=request.POST['limit']
            tweets=GenericSearchTweets(phrase,limit,tweet_type,username)
            if(len(tweets)<1):
                messages.error(request,'Query Failed - No Tweets Found ')
                return redirect('/tw/rapid_search')
            else:
                log=Activity_Logger(activity_name='Phrase Only Search --Tweets' ,
                             activity_app='Twitter_Crawler | Rapid Tweets  Search',
                             activity_details="Phrase = "+phrase+" \n Tweet Type = "+tweet_type+" \n Limit = "+limit+"",
                             activity_status='successfull')
                log.save()
                messages.success(request,'Query Successfull ')
                return render(request,'rapid_view_tweets_images.html',{'tweets':tweets})





        elif search_type=='phrase_search_with_username':
            phrase=request.POST['phrase']
            tweet_type=request.POST['tweet_type']
            username=request.POST['username']
            print("######################################################")
            print("Search Type == ",search_type)
            print("Tweets Type == ",tweet_type)
            print("######################################################")
            limit=request.POST['limit']
            tweets=GenericSearchTweets(phrase,limit,tweet_type,username)
            if(len(tweets)<1):
                messages.error(request,'Query Failed - No Tweets Found ')
                return redirect('/tw/rapid_search')
            else:
                log=Activity_Logger(activity_name='Phrase Search With Username --Tweets' ,
                             activity_app='Twitter_Crawler | Rapid Tweets  Search',
                             activity_details="Phrase = "+phrase+" \n Tweet Type = "+tweet_type+" \n Limit = "+limit+" \n Username = "+username+"",
                             activity_status='successfull')
                log.save()
                messages.success(request,'Query Successfull ')
                return render(request,'rapid_view_tweets_images.html',{'tweets':tweets})





        elif search_type=='phrase_location_seacrh':
            phrase=request.POST['phrase']
            tweet_type=request.POST['tweet_type']
            location=request.POST['location']
            radius=request.POST['radius']
            limit=request.POST['limit']
            # get long and lat
            geolocator = Nominatim()
            location1 = geolocator.geocode(location)
            lat=str(location1.latitude)
            lon=str(location1.longitude)
            rad=str(radius)
            string=""+lat+","+lon+","+rad+""
            print("######################################################")
            print("Search Type == ",search_type)
            print("Tweets Type == ",tweet_type)
            print(lat, lon)

            print("Search radius ="+string)
            print("######################################################")

            tweets=LocationSearchTweets(phrase,limit,tweet_type,lat,lon,rad)
            if(len(tweets)<1):
                messages.error(request,'Query Failed - No Tweets Found ')
                return redirect('/tw/rapid_search')
            else:
                log=Activity_Logger(activity_name='Phrase Location Search  --Tweets' ,
                             activity_app='Twitter_Crawler | Rapid Tweets  Search',
                             activity_details="Phrase = "+phrase+" \n Tweet Type = "+tweet_type+" \n Limit = "+limit+" \n Location = "+location+" \n Radius = "+rad+"Km",
                             activity_status='successfull')
                log.save()
                messages.success(request,'Query Successfull ')
                return render(request,'rapid_view_tweets_images.html',{'tweets':tweets})





        elif search_type=='location_seacrh':
            phrase=''
            tweet_type=request.POST['tweet_type']
            location=request.POST['location']
            radius=request.POST['radius']
            limit=request.POST['limit']
            # get long and lat
            geolocator = Nominatim()
            location1 = geolocator.geocode(location)
            lat=str(location1.latitude)
            lon=str(location1.longitude)
            rad=str(radius)
            string=""+lat+","+lon+","+rad+""
            print("######################################################")
            print("Search Type == ",search_type)
            print("Tweets Type == ",tweet_type)
            print(lat, lon)

            print("Search radius ="+string)
            print("######################################################")

            tweets=LocationSearchTweets(phrase,limit,tweet_type,lat,lon,rad)
            if(len(tweets)<1):
                messages.error(request,'Query Failed - No Tweets Found ')
                return redirect('/tw/rapid_search')
            else:
                log=Activity_Logger(activity_name='Location Search  --Tweets' ,
                             activity_app='Twitter_Crawler | Rapid Tweets  Search',
                             activity_details="Tweet Type = "+tweet_type+" \n Limit = "+limit+" '\n Location = "+location+" \n Radius = "+rad+"Km",
                             activity_status='successfull')
                log.save()
                messages.success(request,'Query Successfull ')
                return render(request,'rapid_view_tweets_images.html',{'tweets':tweets})










        elif search_type=='geo_location_search':
            phrase=''
            tweet_type=request.POST['tweet_type']
            lat=str(request.POST['latitude'])
            lon=str(request.POST['longitude'])
            limit=str(request.POST['limit'])
            rad=str(request.POST['radius'])
            string=""+lat+","+lon+","+rad+""
            print("######################################################")
            print("Search Type == ",search_type)
            print("Tweets Type == ",tweet_type)
            print("Search radius ="+string)
            print("######################################################")
            tweets=LocationSearchTweets(phrase,limit,tweet_type,lat,lon,rad)
            if(len(tweets)<1):
                messages.error(request,'Query Failed - No Tweets Found ')
                return redirect('/tw/rapid_search')
            else:
                log=Activity_Logger(activity_name='Geo Location Search  --Tweets' ,
                             activity_app='Twitter_Crawler | Rapid Tweets  Search',
                             activity_details="Tweet Type = "+tweet_type+" \n Limit = "+limit+" \n Latitude = "+lat+" \n Longitude= "+lon+" \n Radius = "+rad+"Km",
                             activity_status='successfull')
                log.save()
                messages.success(request,'Query Successfull ')
                return render(request,'rapid_view_tweets_images.html',{'tweets':tweets})





        elif search_type=='geo_location_phrase_search':
            phrase=request.POST['phrase']
            tweet_type=request.POST['tweet_type']
            lat=str(request.POST['latitude'])
            lon=str(request.POST['longitude'])
            limit=str(request.POST['limit'])
            rad=str(request.POST['radius'])
            string=""+lat+","+lon+","+rad+""
            print("######################################################")
            print("Search Type == ",search_type)
            print("Tweets Type == ",tweet_type)
            print("Search radius ="+string)
            print("######################################################")
            tweets=LocationSearchTweets(phrase,limit,tweet_type,lat,lon,rad)
            if(len(tweets)<1):
                messages.error(request,'Query Failed - No Tweets Found ')
                return redirect('/tw/rapid_search')
            else:
                log=Activity_Logger(activity_name='Geo Location Search  --Tweets' ,
                             activity_app='Twitter_Crawler | Rapid Tweets  Search',
                             activity_details="Phrase = "+phrase+" \n Tweet Type = "+tweet_type+" \n Limit = "+limit+" \n Latitude = "+lat+" \n Longitude= "+lon+" \n Radius = "+rad+"Km",
                             activity_status='successfull')
                log.save()
                messages.success(request,'Query Successfull ')
                return render(request,'rapid_view_tweets_images.html',{'tweets':tweets})


    return render(request,'rapidsearch.html')






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



# Rapid Search Methods
# phrase search + Phrase search with username
def GenericSearchTweets(_phrase,_limit,_tweet_type,_username):

    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    c.Store_object = True
    c.Search = ""+_phrase
    if _username!='':
        c.Username=_username
    c.Limit =_limit
    print(_tweet_type)
    if _tweet_type =='both':
        # c.Images = True
        c.Images = False
        print("image=false")
    if _tweet_type=='img':
        c.Images = True
        print("image=true")
    if _tweet_type=='text':
        c.Images = False
        print("image=false")
    c.Hide_output = True
# lists
    id=[]
    id_str=[]
    conversation_id=[]
    datetime=[]
    datestamp=[]
    timestamp=[]
    user_id=[]
    user_id_str=[]
    username=[]
    name=[]
    place=[]
    timezone=[]
    img=[]
    mentions=[]
    urls=[]
    photos=[]
    video=[]
    text=[]
    hashtags=[]
    cashtags=[]
    replies_count=[]
    retweets_count=[]
    likes_count=[]
    link=[]
    user_rt_id=[]
    retweet=[]
    retweet_id=[]
    retweet_date=[]
    quote_url=[]
    near=[]
    geo=[]
    source=[]
    reply_to=[]
# Search starts here
    twint.output.clean_lists()
    twint.run.Search(c)
    tweets = twint.output.tweets_list
    for tweet in tweets:
      id.append(tweet.id)
      id_str.append(tweet.id_str)
      conversation_id.append(tweet.conversation_id)
      datetime.append(tweet.datetime)
      datestamp.append(tweet.datestamp)
      timestamp.append(tweet.timestamp)
      user_id.append(tweet.user_id)
      user_id_str.append(tweet.user_id_str)
      username.append(tweet.username)
      name.append(tweet.name)
      place.append(tweet.place)
      timezone.append(tweet.timezone)
      mentions.append(tweet.mentions)
      urls.append(tweet.urls)
      photos.append(tweet.photos)
      video.append(tweet.video)
      text.append(tweet.tweet)
      hashtags.append(tweet.hashtags)
      cashtags.append(tweet.cashtags)
      replies_count.append(tweet.replies_count)
      retweets_count.append(tweet.retweets_count)
      likes_count.append(tweet.likes_count)
      link.append(tweet.link)
      user_rt_id.append(tweet.user_rt_id)
      retweet.append(tweet.retweet)
      retweet_id.append(tweet.retweet_id)
      retweet_date.append(tweet.retweet_date)
      quote_url.append(tweet.quote_url)
      near.append(tweet.near)
      geo.append(tweet.geo)
      source.append(tweet.source)
      reply_to.append(tweet.reply_to)

    # Construct Dictionary of Tweets
    dic = []
    for item in zip(id,id_str,conversation_id,datetime,
                datestamp,timestamp,user_id,user_id_str,username
                ,name,place,timezone,mentions,urls,photos,
                 video,text,hashtags,cashtags,replies_count,likes_count,retweets_count,link
               ,user_rt_id,retweet,retweet_id,retweet_date,quote_url,near,geo,
                source,reply_to
               ):

        dic.append({
            'id':item[0],
            'id_str':item[1],
            'conversation_id':item[2],
            'datetime':item[3],
            'datestamp':item[4],
            'timestamp':item[5],
            'user_id':item[6],
            'user_id_str':item[7],
            'username':item[8],
            'name':item[9],
            'place':item[10],
            'timezone':item[11],
            'mentions':item[12],
            'urls':item[13],
            'photos':item[14],
            'video':item[15],
            'text':item[16],
            'hashtags':item[17],
            'cashtags':item[18],
            'replies_count':item[19],
            'likes_count':item[20],
            'retweets_count':item[21],
            'link':item[22],
            'user_rt_id':item[23],
            'retweet':item[24],
            'retweet_id':item[25],
            'retweet_date':item[26],
            'quote_url':item[27],
            'near':item[28],
            'geo':item[29],
            'source':item[30],
            'reply_to':item[31],
                })




    return dic



# phrase search + Phrase search with username
def LocationSearchTweets(_phrase,_limit,_tweet_type,_lat,_lon,_rad):


    # # c.Hide_output = True
    # c.Output = True
    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    c.Limit =_limit
    c.Geo=""+_lat+","+_lon+","+_rad+"km"
    if _phrase!='':
        c.Search = ""+_phrase
    # c.Output = False
    c.Store_object = True
    print(_tweet_type)
    if _tweet_type =='both':
        c.Images = False
        print("image=false")
    if _tweet_type=='img':
        c.Images = True
        print("image=true")
    if _tweet_type=='text':
        c.Images = False
        print("image=false")
# lists
    id=[]
    id_str=[]
    conversation_id=[]
    datetime=[]
    datestamp=[]
    timestamp=[]
    user_id=[]
    user_id_str=[]
    username=[]
    name=[]
    place=[]
    timezone=[]
    img=[]
    mentions=[]
    urls=[]
    photos=[]
    video=[]
    text=[]
    hashtags=[]
    cashtags=[]
    replies_count=[]
    retweets_count=[]
    likes_count=[]
    link=[]
    user_rt_id=[]
    retweet=[]
    retweet_id=[]
    retweet_date=[]
    quote_url=[]
    near=[]
    geo=[]
    source=[]
    reply_to=[]
# Search starts here
    twint.output.clean_lists()
    twint.run.Search(c)
    tweets = twint.output.tweets_list
    for tweet in tweets:
      id.append(tweet.id)
      id_str.append(tweet.id_str)
      conversation_id.append(tweet.conversation_id)
      datetime.append(tweet.datetime)
      datestamp.append(tweet.datestamp)
      timestamp.append(tweet.timestamp)
      user_id.append(tweet.user_id)
      user_id_str.append(tweet.user_id_str)
      username.append(tweet.username)
      name.append(tweet.name)
      place.append(tweet.place)
      timezone.append(tweet.timezone)
      mentions.append(tweet.mentions)
      urls.append(tweet.urls)
      photos.append(tweet.photos)
      video.append(tweet.video)
      text.append(tweet.tweet)
      hashtags.append(tweet.hashtags)
      cashtags.append(tweet.cashtags)
      replies_count.append(tweet.replies_count)
      retweets_count.append(tweet.retweets_count)
      likes_count.append(tweet.likes_count)
      link.append(tweet.link)
      user_rt_id.append(tweet.user_rt_id)
      retweet.append(tweet.retweet)
      retweet_id.append(tweet.retweet_id)
      retweet_date.append(tweet.retweet_date)
      quote_url.append(tweet.quote_url)
      near.append(tweet.near)
      geo.append(tweet.geo)
      source.append(tweet.source)
      reply_to.append(tweet.reply_to)

    # Construct Dictionary of Tweets
    dic = []
    for item in zip(id,id_str,conversation_id,datetime,
                datestamp,timestamp,user_id,user_id_str,username
                ,name,place,timezone,mentions,urls,photos,
                 video,text,hashtags,cashtags,replies_count,likes_count,retweets_count,link
               ,user_rt_id,retweet,retweet_id,retweet_date,quote_url,near,geo,
                source,reply_to
               ):

        dic.append({
            'id':item[0],
            'id_str':item[1],
            'conversation_id':item[2],
            'datetime':item[3],
            'datestamp':item[4],
            'timestamp':item[5],
            'user_id':item[6],
            'user_id_str':item[7],
            'username':item[8],
            'name':item[9],
            'place':item[10],
            'timezone':item[11],
            'mentions':item[12],
            'urls':item[13],
            'photos':item[14],
            'video':item[15],
            'text':item[16],
            'hashtags':item[17],
            'cashtags':item[18],
            'replies_count':item[19],
            'likes_count':item[20],
            'retweets_count':item[21],
            'link':item[22],
            'user_rt_id':item[23],
            'retweet':item[24],
            'retweet_id':item[25],
            'retweet_date':item[26],
            'quote_url':item[27],
            'near':item[28],
            'geo':item[29],
            'source':item[30],
            'reply_to':item[31],
                })




    return dic
