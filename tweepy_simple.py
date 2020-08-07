import tweepy
import twitter_credentials

MAX_TWEETS = 100

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#AAPL', rpp=100, lang='en').items(MAX_TWEETS):

    print(tweet.text)
    print("-"*10)
    