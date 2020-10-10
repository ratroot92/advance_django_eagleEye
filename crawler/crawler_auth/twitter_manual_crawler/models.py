from django.db import models
from django.db.models.signals import pre_save,post_save
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from datetime import datetime,date

# geopy imports
import geopy
from geopy import Nominatim


# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync



# Create your models here.
class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_str = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    join_date = models.TextField(blank=True, null=True)
    join_time = models.TextField(blank=True, null=True)
    tweets = models.TextField(blank=True, null=True)
    following = models.TextField(blank=True, null=True)
    followers = models.TextField(blank=True, null=True)
    likes = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    private = models.TextField(blank=True, null=True)
    verified = models.TextField(blank=True, null=True)
    profile_image_url = models.TextField(blank=True, null=True)
    background_image = models.TextField(blank=True, null=True)
    # hex_dig = models.TextField(blank=True, null=True)
    # time_update = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    objects = models.Manager()



def add_locations_in_users_model_after_save(sender,instance,**kwargs):
    print("running post save")
    print(instance.location)
    _address=instance.location
    _id=instance.id
    print(instance)
    geolocator = Nominatim()
    location = geolocator.geocode(_address)
    print(location.latitude, location.longitude)
    user_to_be_updated=Users.objects.filter(id=_id).update(lat=location.latitude,lon=location.longitude)


post_save.connect(add_locations_in_users_model_after_save,sender=Users)











class Followers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    join_date = models.TextField(blank=True, null=True)
    join_time = models.TextField(blank=True, null=True)
    tweets = models.TextField(blank=True, null=True)
    following = models.TextField(blank=True, null=True)
    followers = models.TextField(blank=True, null=True)
    likes = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    is_private = models.TextField(blank=True, null=True)
    is_verified = models.TextField(blank=True, null=True)
    profile_image_url = models.TextField(blank=True, null=True)
    background_image = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    follower_id_fk = models.TextField(blank=True, null=True)
    objects = models.Manager()


def add_locations_in_users_model_after_save_follower(sender,instance,**kwargs):
    print("running post save")
    print(instance.location)
    try:
      if(instance.location !=''):
           _address=instance.location
           _id=instance.id
           print(instance)
           geolocator = Nominatim()
           location = geolocator.geocode(_address)
           print(location.latitude, location.longitude)
           user_to_be_updated=Followers.objects.filter(id=_id).update(lat=location.latitude,lon=location.longitude)
      else:
          pass
    except:
      pass


post_save.connect(add_locations_in_users_model_after_save_follower,sender=Followers)















class Followings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    join_date = models.TextField(blank=True, null=True)
    join_time = models.TextField(blank=True, null=True)
    tweets = models.TextField(blank=True, null=True)
    following = models.TextField(blank=True, null=True)
    followers = models.TextField(blank=True, null=True)
    likes = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    is_private = models.TextField(blank=True, null=True)
    is_verified = models.TextField(blank=True, null=True)
    profile_image_url = models.TextField(blank=True, null=True)
    background_image = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    following_id_fk = models.TextField(blank=True, null=True)
    objects = models.Manager()


def add_locations_after_save_following(sender,instance,**kwargs):
    print("running post save")
    print(instance.location)
    try:
      if(instance.location !=''):
           _address=instance.location
           _id=instance.id
           print(instance)
           geolocator = Nominatim()
           location = geolocator.geocode(_address)
           print(location.latitude, location.longitude)
           user_to_be_updated=Followings.objects.filter(id=_id).update(lat=location.latitude,lon=location.longitude)
      else:
          pass
    except:
      pass


post_save.connect(add_locations_after_save_following,sender=Followings)






# Create your models here.
class Tweets(models.Model):
     id = models.BigIntegerField(primary_key=True)
     id_str = models.TextField(blank=True, null=True)
     conversation_id = models.TextField(blank=True, null=True)
     datetime=models.TextField(blank=True, null=True)
     datestamp=models.TextField(blank=True, null=True)
     timestamp=models.TextField(blank=True, null=True)
     user_id=models.TextField(blank=True, null=True)
     user_id_str=models.TextField(blank=True, null=True)
     username=models.TextField(blank=True, null=True)
     name=models.TextField(blank=True, null=True)
     place=models.TextField(blank=True, null=True)
     timezone=models.TextField(blank=True, null=True)
     # img={};
     mentions=models.TextField(blank=True, null=True)
     urls=models.TextField(blank=True, null=True)
     photos=models.TextField(blank=True, null=True)
     video=models.TextField(blank=True, null=True)
     text=models.TextField(blank=True, null=True)
     hashtags=models.TextField(blank=True, null=True)
     cashtags=models.TextField(blank=True, null=True)
     replies_count=models.TextField(blank=True, null=True)
     likes_count=models.TextField(blank=True, null=True)
     retweets_count=models.TextField(blank=True, null=True)
     link=models.TextField(blank=True, null=True)
     user_rt_id=models.TextField(blank=True, null=True)
     retweet=models.TextField(blank=True, null=True)
     retweet_id=models.TextField(blank=True, null=True)
     retweet_date=models.TextField(blank=True, null=True)
     quote_url=models.TextField(blank=True, null=True)
     near=models.TextField(blank=True, null=True)
     geo=models.TextField(blank=True, null=True)
     source=models.TextField(blank=True, null=True)
     reply_to=models.TextField(blank=True, null=True)
     objects = models.Manager()

# def count_tweets_on_insertion(sender,instance,**kwargs):
#     print("before evry tweets save ")



# pre_save.connect(count_tweets_on_insertion,sender=Tweets)


















# other models
class tweets_target_model(models.Model):



    target_scheudling_chioces=[('','Select Target Scheuling'),
                               ('1hr','Every One Hour'),
                               ('6hr','Every Six Hour'),
                               ('12hr','Every Twelve Hour'),
                               ('24hr','Every Day '),
                             ]
    target_platform = models.CharField(max_length=255,default="twitter")
    target_type =models.CharField(max_length=255,default="tweets_target",)
    twitter_username =models.CharField(max_length=255,primary_key=True)
    target_scheduling=models.CharField(max_length=255,choices=target_scheudling_chioces)
    scanning_status=models.CharField(max_length=255,default="pending")
    tweets_count=models.CharField(max_length=255,default="0")
    created_at = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    objects=models.Manager

class tweets_target_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(tweets_target_form, self).__init__(*args, **kwargs)
            self.fields['target_scheduling'].required = True
            self.fields['target_platform'].required = True
            self.fields['target_type'].required = True
            self.fields['target_platform'].disabled = True
            self.fields['target_type'].disabled = True
            self.fields['scanning_status'].disabled = True
            self.fields['tweets_count'].disabled = True

      class Meta:
            # readonly_fields=('submission_date',)
            model=tweets_target_model
            fields=['target_platform','target_type','twitter_username','target_scheduling','scanning_status','tweets_count']
            # widgets = {
            # 'submission_date': forms.DateInput(attrs={'type': 'date'})
            #}
      def clean_twitter_username(self):
           _twitter_username=self.cleaned_data['twitter_username']
           try:
             match=tweets_target_form.objects.get(twitter_username=_twitter_username)
           except:
             return self.cleaned_data['twitter_username']
           raise validators.ValidationError("target already exsists")


#profiles targets
class profiles_target_model(models.Model):



    target_scheudling_chioces=[('','Select Target Scheuling'),
                               ('1hr','Every One Hour'),
                               ('6hr','Every Six Hour'),
                               ('12hr','Every Twelve Hour'),
                               ('24hr','Every Day '),
                             ]
    target_platform = models.CharField(max_length=255,default="twitter")
    target_type =models.CharField(max_length=255,default="profile_target",)
    twitter_username =models.CharField(max_length=255,primary_key=True)
    target_scheduling=models.CharField(max_length=255,choices=target_scheudling_chioces)
    scanning_status=models.CharField(max_length=255,default="pending")
    tweets_count=models.CharField(max_length=255,default="0")
    followers_count=models.CharField(max_length=255,default="0")
    followings_count=models.CharField(max_length=255,default="0")
    tweets_count=models.CharField(max_length=255,default="0")
    profile_img_url=models.CharField(max_length=255,default="0")
    background_image=models.CharField(max_length=255,default="0")
    username=models.CharField(max_length=255,default="0")
    name=models.CharField(max_length=255,default="0")
    media=models.CharField(max_length=255,default="0")
    location=models.CharField(max_length=255,default="0")
    created_at = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    followers_fkey=models.CharField(max_length=255,default="0")
    objects=models.Manager


class profiles_target_form(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(profiles_target_form, self).__init__(*args, **kwargs)
            self.fields['target_scheduling'].required = True
            self.fields['target_platform'].required = True
            self.fields['target_type'].required = True
            self.fields['target_platform'].disabled = True
            self.fields['twitter_username'].required = True
            self.fields['scanning_status'].disabled = True
            self.fields['tweets_count'].disabled = True
            self.fields['followers_count'].disabled = True
            self.fields['followings_count'].disabled = True
            self.fields['followers_fkey'].disabled = True
            self.fields['profile_img_url'].disabled = True
            self.fields['background_image'].disabled = True
            self.fields['username'].disabled = True
            self.fields['name'].disabled = True
            self.fields['media'].disabled = True
            self.fields['location'].disabled = True

      class Meta:
            # readonly_fields=('submission_date',)
            model=profiles_target_model
            fields=['target_platform','target_type','twitter_username','target_scheduling',
                    'scanning_status','tweets_count','followers_count','followings_count',
                    'followers_fkey','profile_img_url','background_image','username','name',
                    'media','location']
            # widgets = {
            # 'submission_date': forms.DateInput(attrs={'type': 'date'})
            #}
      def clean_twitter_username(self):
           _twitter_username=self.cleaned_data['twitter_username']
           try:
             match=profiles_target_model.objects.get(twitter_username=_twitter_username)
           except:
             return self.cleaned_data['twitter_username']
           raise validators.ValidationError("target already exsists")



class Activity_Logger(models.Model):
    activity_name = models.TextField(blank=True, null=True)
    activity_app = models.TextField(blank=True, null=True)
    activity_details = models.TextField(blank=True, null=True)
    activity_status = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    objects=models.Manager
    class Meta:
        ordering = ['-created_at',]