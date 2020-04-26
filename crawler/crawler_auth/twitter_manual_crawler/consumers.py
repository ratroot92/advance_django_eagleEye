import json
from channels.generic.websocket import WebsocketConsumer
from .tasks import getTweets
from .models import Tweets,tweets_target_model
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




class Count_Tweets(WebsocketConsumer):
    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name+"_sharif"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_group_name)
        self.accept()
        print("#######CONNECTED############")

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("DISCONNECED CODE: ",code)

    def receive(self, text_data=None, bytes_data=None):
        print(" MESSAGE RECEIVED")
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'tweets_insertion',
                "message": message,
                "username": username
            }
        )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'tweets_insertion_socket_close',
                "message": message,
                "username": username
            }
        )

    def tweets_insertion_socket_close(self,event):
        self.disconnect()

    def tweets_insertion(self,event):
        message = event['message']
        username = event['username']
        self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))