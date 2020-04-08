from django.db import models
from django.db.models.signals import pre_save,post_save
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from datetime import datetime,date
# Create your models here.



    
class Twitter_Target(models.Model):
    
                
                
    target_scheudling_chioces=[('','Select Target Scheuling'),
                               ('1hr','Every One Hour'),
                               ('6hr','Every Six Hour'),
                               ('12hr','Every Twelve Hour'),
                               ('24hr','Every Day '),
                             ]
    target_platform = models.CharField(max_length=255,default="twitter")
    target_type =models.CharField(max_length=255,default="twitter_person",) 
    twitter_username =models.CharField(max_length=255,primary_key=True) 
    target_scheduling=models.CharField(max_length=255,choices=target_scheudling_chioces)
    scanning_status=models.CharField(max_length=255,default="pending")
    created_at = models.DateField(auto_now_add=True,auto_now=False,blank=True)
    updated_at = models.DateField(auto_now=True,blank=True)
    objects=models.Manager
    
class Twitter_TargetForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Twitter_TargetForm, self).__init__(*args, **kwargs)
            self.fields['target_scheduling'].required = True
            self.fields['target_platform'].required = True
            self.fields['target_type'].required = True
            self.fields['target_platform'].disabled = True
            self.fields['target_type'].disabled = True
            self.fields['scanning_status'].disabled = True
                
      class Meta: 
            # readonly_fields=('submission_date',)
            model=Twitter_Target
            fields=['target_platform','target_type','twitter_username','target_scheduling','scanning_status']
            # widgets = {
            # 'submission_date': forms.DateInput(attrs={'type': 'date'})
            #}
      def clean_twitter_username(self):
           _twitter_username=self.cleaned_data['twitter_username']  
           try:
             match=Twitter_Target.objects.get(twitter_username=_twitter_username)
           except:
             return self.cleaned_data['twitter_username']
           raise validators.ValidationError("target already exsists")
    
# def before_Twitter_Target_save(sender,instance,**kwargs):
#     print('submitting twitter_target ')
        
# def after_Twitter_Target_save(sender,instance,**kwargs):
#     print('submitting twitter_target ')
   

    
# pre_save.connect(before_Twitter_Target_save,sender=Twitter_Target)
# post_save.connect(after_Twitter_Target_save,sender=Twitter_Target)

  
    
    
class Favorites(models.Model):
    
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True,related_name='+')
    tweet = models.ForeignKey('Tweets', models.DO_NOTHING, related_name='+')

        #class Meta:
           # managed = False
         #   db_table = 'favorites'
          #  unique_together = (('user', 'tweet'),)


class Followers(models.Model):
    id = models.OneToOneField('Users', models.DO_NOTHING, db_column='id', primary_key=True,related_name='+')
    follower = models.ForeignKey('Users', models.DO_NOTHING, related_name='+')

    #class Meta:
       # managed = False
     #   db_table = 'followers'
      #  unique_together = (('id', 'follower'),)


class FollowersNames(models.Model):
    user = models.CharField(max_length=100,primary_key=True)
    time_update = models.IntegerField()
    follower = models.TextField()

    #class Meta:
       # managed = False
     #   db_table = 'followers_names'
      #  unique_together = (('user', 'follower'),)


class Following(models.Model):
    id = models.OneToOneField('Users', models.DO_NOTHING, db_column='id', primary_key=True,related_name='+')
    following = models.ForeignKey('Users', models.DO_NOTHING, related_name='+')

    #class Meta:
       # managed = False
     #   db_table = 'following'
      #  unique_together = (('id', 'following'),)


class FollowingNames(models.Model):
    user = models.CharField(max_length=100,primary_key=True)
    time_update = models.IntegerField()
    follows = models.TextField()

    #class Meta:
       # managed = False
     #   db_table = 'following_names'
      #  unique_together = (('user', 'follows'),)


class Replies(models.Model):
    tweet = models.ForeignKey('Tweets', models.DO_NOTHING, related_name='+')
    user_id = models.BigIntegerField(primary_key=True)
    username = models.TextField()

    #class Meta:
       # managed = False
     #   db_table = 'replies'
      #  unique_together = (('user_id', 'tweet'),)


class Retweets(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True,related_name='+')
    username = models.TextField()
    tweet = models.ForeignKey('Tweets', models.DO_NOTHING, related_name='+')
    retweet_id = models.BigIntegerField()
    retweet_date = models.BigIntegerField()

    #class Meta:
       # managed = False
     #   db_table = 'retweets'
      #  unique_together = (('user', 'tweet'),)


class Tweets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_str = models.TextField()
    tweet = models.TextField(blank=True, null=True)
    conversation_id = models.TextField()
    created_at = models.BigIntegerField()
    date = models.TextField()
    time = models.TextField()
    timezone = models.TextField()
    place = models.TextField(blank=True, null=True)
    replies_count = models.IntegerField(blank=True, null=True)
    likes_count = models.IntegerField(blank=True, null=True)
    retweets_count = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    user_id_str = models.TextField()
    screen_name = models.TextField()
    name = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    mentions = models.TextField(blank=True, null=True)
    hashtags = models.TextField(blank=True, null=True)
    cashtags = models.TextField(blank=True, null=True)
    urls = models.TextField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    quote_url = models.TextField(blank=True, null=True)
    video = models.IntegerField(blank=True, null=True)
    geo = models.TextField(blank=True, null=True)
    near = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    time_update = models.BigIntegerField()
    translate = models.TextField(blank=True, null=True)
    trans_src = models.TextField(blank=True, null=True)
    trans_dest = models.TextField(blank=True, null=True)

    #class Meta:
       # managed = False
     #   db_table = 'tweets'
#

class Users(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_str = models.TextField()
    name = models.TextField(blank=True, null=True)
    username = models.TextField()
    bio = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    join_date = models.TextField()
    join_time = models.TextField()
    tweets = models.IntegerField(blank=True, null=True)
    following = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    media = models.IntegerField(blank=True, null=True)
    private = models.IntegerField()
    verified = models.IntegerField()
    profile_image_url = models.TextField()
    background_image = models.TextField(blank=True, null=True)
    hex_dig = models.TextField()
    time_update = models.BigIntegerField()

    #class Meta:
       # managed = False
     #   db_table = 'users'
      #  unique_together = (('id', 'hex_dig'),)



# class Tweets_Model(models.Model):
#     t_id = models.TextField(max_length=100,null=True)
#     t_conversation_id = models.TextField(max_length=100,null=True)
#     t_datetime= models.TextField(max_length=100,null=True)
#     t_datestamp= models.TextField(max_length=100,null=True)
#     t_timestamp= models.TextField(max_length=100,null=True)
#     t_user_id= models.TextField(max_length=100,null=True)
#     t_username= models.TextField(max_length=100,null=True)
#     t_name= models.TextField(max_length=100,null=True)
#     t_place= models.TextField(max_length=100,null=True)
#     t_timezone= models.TextField(max_length=100,null=True)
#     t_mentions= models.TextField(max_length=100,null=True)
#     t_urls= models.TextField(max_length=100,null=True)
#     t_photos= models.TextField(max_length=100,null=True)
#     t_video= models.TextField(max_length=100,null=True)
#     t_tweet= models.TextField(null=True)
#     t_hashtags= models.TextField(null=True)
#     t_cashtags= models.TextField(null=True)
#     t_replies_count= models.TextField(null=True)
#     t_retweets_count= models.TextField(null=True)
#     t_link= models.TextField(null=True)
#     t_likes_count= models.TextField(null=True)
#     t_retweet= models.BooleanField(null=True)
#     t_retweet_id= models.TextField(max_length=100,null=True)
#     t_retweet_date= models.TextField(max_length=100,null=True)
#     t_retweet_id= models.TextField(max_length=100,null=True)
#     t_quote_url= models.TextField(max_length=100,null=True)
#     t_near= models.TextField(max_length=100,null=True)
#     t_geo= models.TextField(max_length=100,null=True)    
#     t_source= models.TextField(max_length=100,null=True)
#     t_reply_to= models.TextField(max_length=100,null=True)  