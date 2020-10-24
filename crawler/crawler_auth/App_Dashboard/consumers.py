import json
from Data_Acquisition_App.Trends_24 import Twitter_Trends
from channels.generic.websocket import WebsocketConsumer
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
        elif(data['opCode'] == 1):
            topTrends=Obj.Pakistan_Top_Trends()
        self.send(text_data=json.dumps({
            '_request': 'Django Twitter Consumer Replying To : ws://127.0.0.1:8001/topTrends/',
            'opCode': 0,
            '_data':topTrends,
            '_status_code': 0,
        }))