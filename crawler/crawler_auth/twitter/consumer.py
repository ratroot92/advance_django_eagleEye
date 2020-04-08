# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
from .tasks import asd
from .models import Tweets

class TwtterConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        _username = text_data_json['_username']
        print(_username)
        Tweets.objects.all().delete()
        r=asd.delay(_username)
        self.send(text_data=json.dumps({
            '_username': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8000/scan/maliksblr92/'
        }))
