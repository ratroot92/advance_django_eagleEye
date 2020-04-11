# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from .tasks import asd,twitterProfileScan
from .models import Tweets,Twitter_Target
from .models import Twitter_Target_Profile
from django.http import JsonResponse
class TwtterConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _username = text_data_json['_username']
        get_user=Twitter_Target.objects.get(twitter_username=_username)
        print(get_user.twitter_username)
        if(get_user.scanning_status=='pending' ):
            Tweets.objects.filter(screen_name=_username).delete()
            r=asd.delay(_username)
            self.send(text_data=json.dumps({
            '_username': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/scan/maliksblr92/',
            '_reply': 'success',
            '_status_code': 0,
        }))
        else:
            self.send(text_data=json.dumps({
            '_username': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/scan/maliksblr92/',
            '_reply': 'failure / request rejected / already completed ',
            '_status_code': 1,
        }))
            
        
class TweetCount(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _username = text_data_json['_username']
        tweets_count=0;
        get_user=Twitter_Target.objects.get(twitter_username=_username)
        print(get_user.twitter_username)
        if(get_user.scanning_status=='completed' or get_user.scanning_status=='pending' ):
        #if(get_user.scanning_status=='pending' ):
            tweets_count = Tweets.objects.filter(screen_name=_username).count()
            print(tweets_count)
            if(tweets_count<=0):
                # t = Twitter_Target.objects.get(twitter_username=_username)
                # t.scanning_status = 'pending' 
                # t.save() 
                self.send(text_data=json.dumps({
            '_message': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/getCount/',
            '_tweets_count':0,
        }))
        
        self.send(text_data=json.dumps({
            '_message': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/getCount/',
            '_tweets_count':tweets_count,
        }))
        
  #pprofile scan 
  
  
class ProfileScan(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _username = text_data_json['_username']
        get_user=Twitter_Target_Profile.objects.get(twitter_username=_username)
        print(get_user.twitter_username)
        if(get_user.scanning_status=='completed' or get_user.scanning_status=='pending' ):
        #if(get_user.scanning_status=='pending' ):
            # tweets_count = Tweets.objects.filter(screen_name=_username).count()
            # print(tweets_count)
            # if(tweets_count<=0):
                # t = Twitter_Target_Profile.objects.get(twitter_username=_username)
                # t.scanning_status = 'pending' 
                # t.save() 
                # self.send(text_data=json.dumps({
            # '_message': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/twitter/profile_scan/',
            # '_tweets_count':0,
        # }))
            r=twitterProfileScan.delay(_username)
            self.send(text_data=json.dumps({
            '_message': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/twitter/profile_scan/',
            '_followers_count':'0',
        }))          
        
