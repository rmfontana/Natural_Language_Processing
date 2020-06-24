import json
import tweepy
import config
from tweepy import OAuthHandler

consumer_key = config.key
consumer_secret = config.csecret
access_token = config.token
access_secret = config.asecret

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

#Users = ["realDonaldTrump", "BarlowforMayor", "NYGovCuomo", "SenSchumer", "KathyMSheehan", "BilldeBlasio", "ScottSingerUSA", "lennycurry", "RonDeSantisFL", "SenRubioPress", "marcorubio", "leoelongworth", "ericgarcetti", "RitterJudy", "thom_bogue", "GavinNewsom", "SenFeinstein", "gregstantonaz", "skiphall2", "dougducey", "SenMcSallyAZ", "SylvesterTurner", "mayorflippo", "StephenForWF", "GregAbbott_TX", "tedcruz", "mayorgarino"]
#Users= ["realDonaldTrump"]
Users = ["BarlowforMayor"]

for user in Users:
        file = user + ".txt"
        user_dict = {}
        user_count = 1
        for status in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode='extended').items(1000):
                # Process a single status # print(status.full_text) # print(json.dumps(status._json))
                user_dict[user_count] = json.dumps(status.full_text)
                user_count += 1
        with open(file, 'a+') as f:
                f.write(json.dumps(user_dict))
