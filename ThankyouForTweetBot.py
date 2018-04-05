# Dependencies
import tweepy
import time
import json
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

target_term = "@redhotmarket"
id_list=[]
def ThankYou():

    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:
        screen_name=tweet["user"]["screen_name"]
        tweet_id=tweet["id"]
        try:
            if(tweet_id in id_list):
                          print("Already tweeted")
            else:
                          id_list.append(tweet_id)
                          api.update_status(f"@{screen_name} Thank you for your tweet.",in_reply_to_status_id=tweet_id)
                          print(f"Replied to {screen_name}")
        except:
                          print("Already tweeted.Ignoring")
while(True):
    ThankYou()
    time.sleep(300)