# from celery import shared_task
# from celery.utils.log import get_task_logger

# logger=get_task_logger(__name__)

# # This is the decorator which a celery worker uses
# # @shared_task(name="getTweets_all")
# @shared_task()
# def getTweets_async(username):
#     logger.info("tweets scrapping started for "+username)
#     getTweets_all(username)
#     return True


# 
# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import json
import twint
import asyncio
import nest_asyncio
from .models import Twitter_Target,Twitter_Target_Profile
import subprocess
@shared_task
def asd(_username):
    c = twint.Config()
    c.Username = _username
#    c.Limit = 20
    c.Store_object = True
    c.Hide_output = False
    c.Database = "d_auth"
   # nest_asyncio.apply()
    twint.run.Search(c)
    t = Twitter_Target.objects.get(twitter_username=_username)
    t.scanning_status = 'completed' 
    t.save() 
    #status=subprocess.run('celery -A twitter control shutdown',shell=True)
    print("status.asd.ENDED")
    




    # tweet_text = []
    # tweet_id = []
    # tweet_date_timestamp = []
    # tweet_timestamp = []
    # tweet_userid = []
    # tweet_username = []
    # tweet_tweet_name = []
    # tweet_time_zone = []
    # tweet_replies_count = []
    # tweet_retweet_count = []
    # tweet_link = []
    # tweet_like_count = []
    # tweet_retweet_status = []
    # tweet_quote_url = []

    # twint.run.Search(c)
    # tweets = twint.output.tweets_list
    # for tweet in tweets:
    #     tweet_text.append(format(tweet.tweet))
    #     tweet_id.append(format(tweet.id))
    #     tweet_date_timestamp.append(format(tweet.datestamp))
    #     tweet_timestamp.append(format(tweet.timestamp))
    #     tweet_userid.append(format(tweet.user_id_str))
    #     tweet_username.append(format(tweet.username))
    #     tweet_tweet_name.append(format(tweet.name))
    #     tweet_time_zone.append(format(tweet.timezone))
    #     tweet_replies_count.append(format(tweet.replies_count))
    #     tweet_retweet_count.append(format(tweet.retweets_count))
    #     tweet_like_count.append(format(tweet.likes_count))
    #     tweet_link.append(format(tweet.link))
    #     tweet_retweet_status.append(format(tweet.retweet))
    #     tweet_quote_url.append(format(tweet.quote_url))
    # dic = []
    # for item in zip(tweet_text, tweet_id, tweet_date_timestamp, tweet_timestamp, tweet_userid, tweet_username, tweet_tweet_name, tweet_time_zone, tweet_replies_count, tweet_retweet_count, tweet_link, tweet_like_count, tweet_retweet_status, tweet_quote_url):

    #     dic.append({
    #         'tweet_text': item[0],
    #         'tweet_id': item[1],
    #         'tweet_date_timestamp': item[2],
    #         'tweet_timestamp': item[3],
    #         'tweet_userid': item[4],
    #         'tweet_username': item[5],
    #         'tweet_tweet_name': item[6],
    #         'tweet_time_zone': item[7],
    #         'tweet_replies_count': item[8],
    #         'tweet_retweet_count': item[9],
    #         'tweet_link': item[10],
    #         'tweet_like_count': item[11],
    #         'tweet_retweet_status': item[12],
    #         'tweet_quote_url': item[13],
    #     })
    # print(dic)
    # # target=Tweets_Model(
    # #     t_tweet=target_type,
    # #     t_id=target_platform,
    # #     t_datetime=twitter_username,
    # #     t_timestamp=submission_date,
    # #     t_user_id=submission_date,
    # #     t_username=target_scheduling,
    # #     t_name=target_type,
    # #     t_timezone=target_platform,
    # #     t_retweets_count=twitter_username,
    # #     t_link=submission_date,
    # #    )
    # # target.save()


@shared_task
def twitterProfileScan_Followers(_username):
    # nest_asyncio.apply()
    c = twint.Config()
    c.Username = _username
    c.User_full = True
    c.Store_object = True
    c.Database = "d_auth"  
    twint.run.Followers(c)  
    # twint.run.Following(c)
    #t = Twitter_Target_Profile.objects.get(twitter_username=_username)
    #t.scanning_status = 'completed' 
    # t.save() 
    # status=subprocess.run('celery -A twitter control shutdown',shell=True)
    print("status.twitterProfileScan_Followers.ENDED");

@shared_task
def twitterProfileScan_Following(_username):
    # nest_asyncio.apply()
    c = twint.Config()
    c.Username = _username
    c.User_full = True
    c.Store_object = True
    c.Database = "d_auth"  
    twint.run.Following(c)
    t = Twitter_Target_Profile.objects.get(twitter_username=_username)
    t.scanning_status = 'completed' 
    t.save() 
    # status=subprocess.run('celery -A twitter control shutdown',shell=True)
    print("status.twitterProfileScan_Following.ENDED");

















