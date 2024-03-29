import tweepy
import getopt, sys
import mariadb
from datetime import datetime, timedelta, timezone
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

consumer_key = '-------'
consumer_secret = '-------'
access_token = '-------'
access_secret = '--------'
tweetsPerQry = 10
maxTweets = 200
for arg in sys.argv:
    print(arg)
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
mycursor = mydb.cursor()
newTweets = tweepy.Cursor(api.search_tweets, q=hashtag).items(maxTweets)

newTweets = [x for x in newTweets]

total = 0
val = []
for tweet in newTweets:
    text = tweet.text
    user_screen_name = tweet.user.screen_name
    tweet_tuple = (
        user_screen_name,
        text
    ) 
    query = "SELECT * FROM ftweet WHERE text_raw=%s"
    mycursor.execute(query, (text,))

    x = [i for i in mycursor]

    if x == []:
        # print(str(id)+":"+str(text)+"\n\n")
        val.append(tweet_tuple)

sql = '''
    INSERT INTO ftweet (username, text_raw) 
    VALUES (%s,%s)
'''
mycursor.executemany(sql, val)

mydb.commit()
tweetCount += len(newTweets)	
maxId = newTweets[-1].id