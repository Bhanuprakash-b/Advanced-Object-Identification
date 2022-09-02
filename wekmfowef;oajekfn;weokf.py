from tweepy import *
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key ="BhanuNameis"
consumer_secret = "Bhanu@143"
access_key= "Luci"
access_secret = "Luci2"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "#bitcoin"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])

