import tweepy

import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)


'''

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='elonmusk').items(10):
    print(tweet.text)
'''