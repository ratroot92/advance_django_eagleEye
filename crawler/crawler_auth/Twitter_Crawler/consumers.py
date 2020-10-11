import json
from channels.generic.websocket import WebsocketConsumer
from .tasks import getTweets,getAllFollowers,getSingleUser,getAllFollowings
from .models import Tweets,tweets_target_model
from .models import profiles_target_model
from django.http import JsonResponse
from asgiref.sync import async_to_sync
class Twitter_Tweets_Targets_Channels(WebsocketConsumer):
    # chat/consumers.py


    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _username = text_data_json['_username']
        get_user=tweets_target_model.objects.get(twitter_username=_username)
        print(get_user.twitter_username)
        if(get_user.scanning_status=='pending' or get_user.scanning_status=='completed'):
            t=tweets_target_model.objects.get(twitter_username=_username)
            t.scanning_status = 'pending'
            t.save()
            r=getTweets.delay(_username)
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
        get_user=tweets_target_model.objects.get(twitter_username=_username)
        print(get_user.twitter_username)
        if(get_user.scanning_status=='completed' or get_user.scanning_status=='pending' ):
        #if(get_user.scanning_status=='pending' ):
            tweets_count = Tweets.objects.filter(screen_name=_username).count()
            print(tweets_count)
            if(tweets_count<=0):
                # t = tweets_target_model.objects.get(twitter_username=_username)
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







class Rescan_Twitter_Profile_Target(WebsocketConsumer):



    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _username = text_data_json['_username']
        get_user=profiles_target_model.objects.get(twitter_username=_username)
        print(get_user.twitter_username)
        if(get_user.scanning_status=='pending' or get_user.scanning_status=='completed'):
            t=profiles_target_model.objects.get(twitter_username=_username)
            t.scanning_status = 'pending'
            t.save()
            s=getSingleUser.delay(_username)
            r=getAllFollowers.delay(_username)
            t=getAllFollowings.delay(_username)
            self.send(text_data=json.dumps({
            '_username': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/rescan/profile_targets/',
            '_reply': 'success',
            '_status_code': 0,
        }))
        else:
            self.send(text_data=json.dumps({
            '_username': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/rescan/profile_targets/',
            '_reply': 'failure / request rejected / already completed ',
            '_status_code': 1,
        }))


class CELERY_NOTIFICATIONS_Twitter_Crawler(WebsocketConsumer):
    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name+"_sharif"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_group_name)
        self.accept()
        print("###############CELERY NOTIFICATIONS CHANNEL  CONNECTED ##########################")

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("########### CELERY NOTIFICATIONS CHANNEL DISCONNECED CODE: ##############",code)

    def receive(self, text_data=None, bytes_data=None):
        print("###############CELERY NOTIFICATIONS RECEIVED ##########################")
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        info = data['info']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'tweets_insertion',
                "message": message,
                "username": username,
                "info": info
            }
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'tweets_insertion_socket_close',
                "message": message,
                "username": username
            }
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'followers_scanning_complete',
                "message": message,
                "username": username,
                "info": info,
            }
        )
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'following_scanning_complete',
                "message": message,
                "username": username,
                "info": info,
            }
        )

    def tweets_insertion_socket_close(self,event):
        self.disconnect()

    def followers_scanning_complete(self,event):
        print("############### CELERY =  followers_scanning_complete ##########################")
        message = event['message']
        username = event['username']
        info=event['info']
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'info':info,
        }))
    def following_scanning_complete(self,event):
        print("############### CELERY =  following_scanning_complete ##########################")
        message = event['message']
        username = event['username']
        info=event['info']
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'info':info,
        }))
    def tweets_insertion(self,event):
        print("############### CELERY =  tweets_insertion ##########################")
        message = event['message']
        username = event['username']
        info=event['info']
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
              'info':info,
        }))