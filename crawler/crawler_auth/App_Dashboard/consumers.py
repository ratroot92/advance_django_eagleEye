import json
from Data_Acquisition_App.Trends_24 import Twitter_Trends
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
class Top_Trends(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        Obj= Twitter_Trends()
        if(data['opCode'] == 0 or data['opCode'] == '0'):
            topTrends=Obj.World_Top_Trends()
        if(data['opCode'] == 1 or data['opCode'] == '1'):
            topTrends=Obj.Pakistan_Top_Trends()
        print(data['opCode'])
        self.send(text_data=json.dumps({
            '_request': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8001/topTrends/',
            'opCode': data['opCode'],
            '_data':topTrends,
            '_status_code': 0,
        }))

            
class Top_Trends_By_Location(WebsocketConsumer):
        def connect(self):
            self.room_name = 'schedule'
            self.room_group_name = self.room_name+"UpdateTopTrends"
            async_to_sync(self.channel_layer.group_add)(
                    self.room_group_name,
                    self.channel_name
                )
            self.accept()
            print("***-scheduleUpdateTopTrends(connect)-***")

        def disconnect(self, close_code):
            async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
            )
            print("***-scheduleUpdateTopTrends(disconnect)-***")
       

        def receive(self,message=None, bytes_data=None):
            print("***-scheduleUpdateTopTrends(receive)-***")
            data = json.loads(message)
            async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'updateTopTrends',
            }
        )
        """---"""
        def updateTopTrends(self,data):
            print("updateTopTrends***-updateTopTrends()-***")
            self.send(text_data=json.dumps({
            '_request': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8001/topTrends/',
                '_status_code': 0,
            }))