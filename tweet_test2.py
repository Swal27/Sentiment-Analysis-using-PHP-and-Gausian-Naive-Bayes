import tweepy
import getopt, sys
import mariadb
from datetime import datetime, timedelta, timezone
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

consumer_key = 'SwdcgILvEZaWRyK0IMT2DdAxe'
consumer_secret = '6waeB6lxCtJExj2wtTgjZT0WX5qOrv9DN1Vm6ET86BHRqc1rYA'
access_token = '802299183709372416-mDKPckyQg442t4tFhnZoVytmSmJKwjx'
access_secret = 'CgVg6kco3ftvgJANoalsr1jGJA4KeYExqsuiPbIjxb7Vu'
tweetsPerQry = 10
maxTweets = 100
hashtag = sys.argv[1]

mydb = mariadb.connect(
  host="localhost",
  user="root",
  passwd="",
  database="social_media"
)

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)#, wait_on_rate_limit_notify=True)'
maxId = -1
tweetCount = 0
while tweetCount < maxTweets:
    if(maxId <= 0):
        newTweets = api.search_tweets(q=hashtag, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
    else:
        newTweets = api.search_tweets(q=hashtag, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")

    if not newTweets:
        print("Tweet Habis")
        break

    val = []
    for tweet in newTweets:
        user_screen_name = tweet.user.screen_name
        text = tweet.full_text.encode('utf-8')
        tweet_tuple = (
            user_screen_name,
            text
        ) 
        print(str(id)+":"+str(text)+"\n\n")
        val.append(tweet_tuple)


    mycursor = mydb.cursor()    
    sql = '''
        INSERT INTO ftweet (username, text_raw) 
        VALUES (%s,%s)
    '''
    mycursor.executemany(sql, val)
    mydb.commit()
    tweetCount += len(newTweets)	
    maxId = newTweets[-1].id

    mydb.close()