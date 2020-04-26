
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import json
import twint
import asyncio
import nest_asyncio
from .models import Tweets,Users,tweets_target_model,count_tweets_on_insertion,Followers,profiles_target_model
import subprocess
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
@shared_task
def getTweets(_username):

    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    # c.Username = "maliksblr92"
    c.Username = _username
    c.Store_object = True
    c.Limit =20
    c.Hide_output = True
    # c.Database = "eagle_eye"
    # nest_asyncio.apply()




    id=[]
    id_str=[]
    conversation_id=[]
    datetime=[]
    datestamp=[]
    timestamp=[]
    user_id=[]
    user_id_str=[]
    username=[]
    name=[]
    place=[]
    timezone=[]
    img=[]
    mentions=[]
    urls=[]
    photos=[]
    video=[]
    text=[]
    hashtags=[]
    cashtags=[]
    replies_count=[]
    retweets_count=[]
    likes_count=[]
    link=[]
    user_rt_id=[]
    retweet=[]
    retweet_id=[]
    retweet_date=[]
    quote_url=[]
    near=[]
    geo=[]
    source=[]
    reply_to=[]


    # obj_list=[]
    # obj={
    # "id":"",
    # "id_str":"",
    # "conversation_id":"",
    # "datetime":"",
    # "datestamp":"",
    # "timestamp":"",
    # "user_id":"",
    # "user_id_str":"",
    # "username":"",
    # "name":"",
    # "place":"",
    # "timezone":"",
    # "img":"",
    # "mentions":"",
    # "urls":"",
    # "photos":"",
    # "video":"",
    # "text":"",
    # "hashtags":"",
    # "cashtags":"",
    # "replies_count":"",
    # "likes_count":"",
    # "link":"",
    # "user_rt_id":"",
    # "retweet":"",
    # "retweet_id":"",
    # "retweet_date":"",
    # "quote_url":"",
    # "near":"",
    # "geo":"",
    # "source":"",
    # "reply_to":"",

    # }
    twint.run.Search(c)
    tweets = twint.output.tweets_list
    for tweet in tweets:
          # obj['id']=tweet.id,
          # obj['id_str']=tweet.id_str
          # obj['conversation_id']=tweet.conversation_id
          # obj['datetime']=tweet.datetime
          # obj['datestamp']=tweet.datestamp
          # obj['timestamp']=tweet.timestamp
          # obj['user_id']=tweet.user_id
          # obj['user_id_str']=tweet.user_id_str
          # obj['username']=tweet.username
          # obj['name']=tweet.name
          # obj['place']=tweet.place
          # obj['timezone']=tweet.timezone
          # obj['photos']=tweet.photos
          # obj['mentions']=tweet.mentions
          # obj['urls']=tweet.urls
          # obj['photos']=tweet.photos
          # obj['video']=tweet.video
          # obj['text']=tweet.tweet
          # obj['hashtags']=tweet.hashtags
          # obj['cashtags']=tweet.cashtags
          # obj['replies_count']=tweet.replies_count
          # obj['likes_count']=tweet.likes_count
          # obj['link']=tweet.link
          # obj['user_rt_id']=tweet.user_rt_id
          # obj['retweet']=tweet.retweet
          # obj['retweet_date']=tweet.retweet_date
          # obj['quote_url']=tweet.quote_url
          # obj['link']=tweet.link
          # obj['user_rt_id']=tweet.user_rt_id
          # obj['retweet']=tweet.retweet
          # obj['retweet_date']=tweet.retweet_date
          # obj['quote_url']=tweet.quote_url
          # obj['geo']=tweet.geo
          # obj['source']=tweet.source
          # obj['reply_to']=tweet.reply_to
          # print(type(obj))
          # print(obj)
          # save_tweets=Tweets(tweet_obj=obj)
          # save_tweets.save()

      id.append(tweet.id)
      id_str.append(tweet.id_str)
      conversation_id.append(tweet.conversation_id)
      datetime.append(tweet.datetime)
      datestamp.append(tweet.datestamp)
      timestamp.append(tweet.timestamp)
      user_id.append(tweet.user_id)
      user_id_str.append(tweet.user_id_str)
      username.append(tweet.username)
      name.append(tweet.name)
      place.append(tweet.place)
      timezone.append(tweet.timezone)
      mentions.append(tweet.mentions)
      urls.append(tweet.urls)
      photos.append(tweet.photos)
      video.append(tweet.video)
      text.append(tweet.tweet)
      hashtags.append(tweet.hashtags)
      cashtags.append(tweet.cashtags)
      replies_count.append(tweet.replies_count)
      retweets_count.append(tweet.retweets_count)
      likes_count.append(tweet.likes_count)
      link.append(tweet.link)
      user_rt_id.append(tweet.user_rt_id)
      retweet.append(tweet.retweet)
      retweet_id.append(tweet.retweet_id)
      retweet_date.append(tweet.retweet_date)
      quote_url.append(tweet.quote_url)
      near.append(tweet.near)
      geo.append(tweet.geo)
      source.append(tweet.source)
      reply_to.append(tweet.reply_to)

    print("printing list ")
    dic = []
    for item in zip(id,id_str,conversation_id,datetime,
                datestamp,timestamp,user_id,user_id_str,username
                ,name,place,timezone,mentions,urls,photos,
                 video,text,hashtags,cashtags,replies_count,likes_count,retweets_count,link
               ,user_rt_id,retweet,retweet_id,retweet_date,quote_url,near,geo,
                source,reply_to
               ):

        dic.append({
            'id':item[0],
            'id_str':item[1],
            'conversation_id':item[2],
            'datetime':item[3],
            'datestamp':item[4],
            'timestamp':item[5],
            'user_id':item[6],
            'user_id_str':item[7],
            'username':item[8],
            'name':item[9],
            'place':item[10],
            'timezone':item[11],
            'mentions':item[12],
            'urls':item[13],
            'photos':item[14],
            'video':item[15],
            'text':item[16],
            'hashtags':item[17],
            'cashtags':item[18],
            'replies_count':item[19],
            'likes_count':item[20],
            'retweets_count':item[21],
            'link':item[22],
            'user_rt_id':item[23],
            'retweet':item[24],
            'retweet_id':item[25],
            'retweet_date':item[26],
            'quote_url':item[27],
            'near':item[28],
            'geo':item[29],
            'source':item[30],
            'reply_to':item[31],
                })

    Tweets.objects.filter(username=_username.lower()).all().delete()
    print(_username+": All Previous Tweets Deleted For User : "+_username)
    for i in dic:
        lower_case_username=_username.lower()
        count=Tweets.objects.filter(username=lower_case_username).count()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'event_sharif',
                {
            'type': 'tweets_insertion',
            'message': count,
            'username': _username,
                }
                )
        print(count)
        tweet=Tweets(
            id =i['id'],
            id_str = i['id_str'],
            conversation_id = i['conversation_id'],
            datetime=i['datetime'],
            datestamp=i['datestamp'],
            timestamp=i['timestamp'],
            user_id=i['user_id'],
            user_id_str=i['user_id_str'],
            username=i['username'],
            name=i['name'],
            place=i['place'],
            timezone=i['timezone'],
            # img={};
            mentions=i['mentions'],
            urls=i['urls'],
            photos=i['photos'],
            video=i['video'],
            text=i['text'],
            hashtags=i['hashtags'],
            cashtags=i['cashtags'],
            replies_count=i['replies_count'],
            likes_count=i['likes_count'],
            retweets_count=i['retweets_count'],
            link=i['link'],
            user_rt_id=i['user_rt_id'],
            retweet=i['retweet'],
            retweet_id=i['retweet_id'],
            retweet_date=i['retweet_date'],
            quote_url=i['quote_url'],
            near=i['near'],
            geo=i['geo'],
            source=i['source'],
            reply_to=i['reply_to'],
                )
        tweet.save()

    lower_case_username=_username.lower()
    tweets_counts=Tweets.objects.filter(username=lower_case_username).count()
    t=tweets_target_model.objects.get(twitter_username=_username)
    t.scanning_status = 'completed'
    t.tweets_count=tweets_counts
    t.save()
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
            'event_sharif',
                {
            'type': 'tweets_insertion_socket_close',
            'message': 'scanning complete ! socket closed ',
            'username': _username,
                }
                )


@shared_task
def getAllFollowers(_username):
    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    c.Username = _username
    c.User_full = True
    c.Store_object = True
    twint.run.Followers(c)
    user_lists = twint.output.users_list

    id=[]
    name =[]
    username  =[]
    bio  =[]
    location =[]
    url  =[]
    join_date  =[]
    join_time=[]
    tweets  =[]
    following =[]
    followers =[]
    likes    =[]
    profile_image_url =[]
    is_private  =[]
    is_verified =[]
    media =[]
    background_image =[]

    for user in user_lists:
        id.append(user.id)
        name.append(user.name)
        username.append(user.username)
        bio.append(user.bio)
        location.append(user.location)
        url.append(user.url)
        join_date.append(user.join_date)
        join_time.append(user.join_time)
        tweets.append(user.tweets)
        following.append(user.following)
        followers.append(user.followers)
        likes.append(user.likes)
        profile_image_url.append(user.avatar)
        is_private.append(user.is_private )
        is_verified.append(user.is_verified)
        media.append(user.media_count)
        background_image.append(user.background_image)
    dic = []
    for item in zip(id,name,username,bio,location,url,join_date,join_time,tweets,following,followers,likes,profile_image_url,is_private,is_verified,media,background_image):

        dic.append({
            'id':item[0],
            'name':item[1],
            'username':item[2],
            'bio':item[3],
            'location':item[4],
            'url':item[5],
            'join_date':item[6],
            'join_time':item[7],
            'tweets':item[8],
            'following':item[9],
            'followers':item[10],
            'likes':item[11],
            'profile_image_url':item[12],
            'is_private':item[13],
            'is_verified':item[14],
            'media':item[15],
            'background_image':item[16],


            })
    get_profile_target_fkey=profiles_target_model.objects.filter(twitter_username=_username).get()
    for i in dic:
        # lower_case_username=_username.lower()
        # count=Tweets.objects.filter(username=lower_case_username).count()
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'event_sharif',
        #         {
        #     'type': 'tweets_insertion',
        #     'message': count,
        #     'username': _username,
        #         }
        #         )
        # print(count)

        followers=Followers(
               id=i['id'],
               name =i['name'],
               username  =i['username'],
               bio  =i['bio'],
               location =i['location'],
               url  =i['url'],
               join_date  =i['join_date'],
               join_time=i['join_time'],
               tweets  =i['tweets'],
               following =i['following'],
               followers =i['followers'],
               likes    =i['likes'],
               profile_image_url =i['profile_image_url'],
               is_private  =i['is_private'],
               is_verified =i['is_verified'],
               media =i['media'],
               background_image =i['background_image'],
               following_id_fk=get_profile_target_fkey.followers_fkey
                )
        followers.save()


















@shared_task
def getSingleUser(_username):
     # nest_asyncio.apply()
    asyncio.set_event_loop(asyncio.new_event_loop())
    c = twint.Config()
    c.Username = _username
    c.Store_object = True
    # user = {'id': ''}
    twint.run.Lookup(c)
    u = twint.output.users_list
    print(u)
    update_profile_target=profiles_target_model.objects.get(twitter_username=_username)
    update_profile_target.followers_fkey=u[0].id
    update_profile_target.followings_count=u[0].following
    update_profile_target.followers_count= u[0].followers
    update_profile_target.tweets_count=u[0].tweets
    update_profile_target.save()
    # user['id'] = format(u[0].id)
    # user['id_str'] = format(u[0].id)
    # user['name'] = u[0].name
    # user['username'] = u[0].username
    # user['bio'] = u[0].bio
    # user['location'] = u[0].location
    # user['url'] = u[0].location
    # user['join_date'] = u[0].join_date
    # user['join_time'] = u[0].join_time
    # user['tweets'] = u[0].tweets
    # user['following'] = u[0].following
    # user['followers'] = u[0].followers
    # user['likes'] = u[0].likes
    # user['media'] = u[0].media_count
    # user['is_private'] = u[0].is_private
    # user['is_verified'] = u[0].is_verified
    # user['profile_image_url'] = u[0].avatar
    # user['background_image'] = u[0].background_image













