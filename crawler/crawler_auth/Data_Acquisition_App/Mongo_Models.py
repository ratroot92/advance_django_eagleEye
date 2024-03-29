from mongoengine import *
from mongoengine import connect
from django.conf import settings

MONGO_DB_IP = settings.MONGO_DB

import datetime
import os
disconnect('default')
#CONNECT TO MONGO DB
connect(db='Eagle_Eye',host=MONGO_DB_IP, port=27017)

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
""" """
PERIODIC_INTERVALS = (
        (0,('one time only')),
        (5,('once per 5 minutes ')),
        (10, ('once per 10 minutes ')),
        (15, ('once per 15 minutes ')),
        (30, ('once per 30 minutes ')),
        (40, ('once per 40 minutes ')),
        (60, ('once per 60 minutes ')),
        (90, ('once per 90 minutes ')),
        (120, ('once per 120 minutes ')),
        (180, ('once per 180 minutes ')),
        (360, ('once per 360 minutes ')),
        (720, ('once per 720 minutes ')),
    )




class Twitter_Target_Document(Document):
    target_platform       =StringField(verbose_name="Target_Platform", max_length=255,default="twitter")
    target_type           =StringField(verbose_name="Target_Type",default="tweets")
    target_username       =StringField(verbose_name="Target_Username")
    target_scheduling     =IntField(verbose_name="Target_Scheduling",choices=PERIODIC_INTERVALS,default=0)
    scanning_status       =StringField(verbose_name="Scanning_Status",default="pending")
    #field to be updated later 
    tweets                =ListField(verbose_name="Tweets",default=[])
    tweets_count          =IntField(verbose_name="Tweets_Count",default=0)
    created_at            =DateField(default=datetime.datetime.now, editable=False,)
    updated_at            =DateField(default=datetime.datetime.now, editable=True,)
    def __repr__(self):
        return self.target_username
    def __str__(self):
        return self.target_username
    """ Create / Insert """
    def Create_Twitter_Target(self,target_platform,target_type,target_username,target_scheduling):
        self.target_platform=str(target_platform)
        self.target_type=str(target_type)
        self.target_username=str(target_username)
        self.target_scheduling=int(target_scheduling)
        try:
           self.save()
           print(f"{bcolors.WARNING}Twitter Target Document  --Create_Twitter_Target  --Success ,{bcolors.ENDC}")
           return True
        except Exception as e:
          print(f"{bcolors.WARNING}Twitter Target Document  --Create_Twitter_Target  --Exception ,{bcolors.ENDC}")
          print(e)
          return False

    """ returns all twitter targets """
    @staticmethod
    def Get_All_Twitter_Targets():
        try:
            Targets=Twitter_Target_Document.objects.all()
            return Targets
        except Exception as e:
            print("Get_All_Twitter_Targets --failed")
            print(e) 
    @staticmethod
    def UserExist(target_username):
        targetExist=Twitter_Target_Document.objects.filter(target_username=target_username)
        if(targetExist):
            print(f"{bcolors.WARNING}Twitter Target Document  --UserExist  --Target Already Exist ,{bcolors.ENDC}")
            return True
        else:
            print(f"{bcolors.WARNING}Twitter Target Document  --UserExist  --Target Not Exiist ,{bcolors.ENDC}")
            return False

    @staticmethod
    def FindTarget(target_username):
        targetExist=Twitter_Target_Document.objects.filter(target_username=target_username).first()
        if(targetExist):
            print(f"{bcolors.WARNING}Twitter Target Document  --FindTarget  --Success ,{bcolors.ENDC}")
            return targetExist
        else:
            print(f"{bcolors.WARNING}Twitter Target Document  --FindTarget  --Failed ,{bcolors.ENDC}")
            return False

    @staticmethod
    def InsertTargetTweets(target_username,tweets_list):
        targetExist=Twitter_Target_Document.objects.filter(target_username=target_username).first()
        if(targetExist):
            #this will first empty the tweets_list on db  and save new tweets 
            targetExist.update(add_to_set__tweets=[])
            targetExist.update(add_to_set__tweets=tweets_list)
           #print(int(len(tweets_list)))scanning_status="completed"
            targetExist.update(scanning_status="completed",tweets_count=len(tweets_list))
            # targetExist.tweets_count+=int(len(tweets_list))
            targetExist.save()
            print(f"{bcolors.WARNING}Twitter Target Document  --InsertTargetTweets  --Success ,{bcolors.ENDC}")
            return True
        else:
            print(f"{bcolors.WARNING}Twitter Target Document  --InsertTargetTweets  --Failed ,{bcolors.ENDC}")
            return False




class Top_World_Trends(Document):
    trends      =ListField(default=[])
    created_at  =DateField(default=datetime.datetime.now, editable=False,)
    updated_at  =DateField(default=datetime.datetime.now, editable=True,)
    def Create(self,trends):
        self.trends=trends
        try:
           self.save()
           print(f"{bcolors.WARNING}Top_World_Trends  --Create  --Success ,{bcolors.ENDC}")
           return True
        except Exception as e:
          print(f"{bcolors.WARNING}Top_World_Trends  --Create  --Exception ,{bcolors.ENDC}")
          print(e)
          return False

class Countries_Top_Trends_Document(Document):
    country_name=StringField(verbose_name="Country_Name", max_length=255,default="")
    city_name=StringField(verbose_name="City_Name", max_length=255,default="")
    trends      =ListField(default=[])
    created_at  =DateField(default=datetime.datetime.now, editable=False,)
    updated_at  =DateField(default=datetime.datetime.now, editable=True,)
    def Create(self,country_name,city_name,trends):
        self.city_name=city_name
        self.country_name=country_name
        self.trends=trends
        try:
           self.save()
           print(f"{bcolors.WARNING}Top_World_Trends  --Create Countries_Top_Trends_Document --Success ,{bcolors.ENDC}")
           return True
        except Exception as e:
          print(f"{bcolors.WARNING}Top_World_Trends  --Create Countries_Top_Trends_Document --Exception ,{bcolors.ENDC}")
          print(e)
          return False
    @staticmethod
    def getPakistanTrends():
        topTrends=Countries_Top_Trends_Document.objects.filter(country_name="pakistan")
        return topTrends