from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import json
import subprocess
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from Data_Acquisition_App.Trends_24 import Twitter_Trends
from Data_Acquisition_App.Mongo_Models import Top_World_Trends


