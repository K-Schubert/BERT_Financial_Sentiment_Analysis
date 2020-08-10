class TweetCollector():
	"""
	Class for collecting and processing tweets.
	"""

	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def collect_tweets(self, hashtag, max_tweets):
		tweets = []
		for tweet in tweepy.Cursor(api.search, q=hashtag, lang='en').items(MAX_TWEETS):
			tweets.append(tweet)

		return tweets

	def tweets_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

		df['id'] = np.array([tweet.id for tweet in tweets])
		df['len'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

		return df

	def analyze_sentiment(self, tweet):
		analysis = TextBlob(tweet)
		
		'''
		if analysis.sentiment.polarity > 0:
			return 1
		elif analysis.sentiment.polarity == 0:
			return 0
		else:
			return -1
		'''

		return analysis.sentiment.polarity

MAX_TWEETS = 10000
since = '2020-08-06'
until = '2020-08-08'

auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
api = tweepy.API(auth)

tweet_collector = TweetCollector()

tweets = tweet_collector.collect_tweets(hashtag="#AAPL since:{} until:{}".format(since, until), max_tweets=MAX_TWEETS)
tweets_df = tweet_collector.tweets_to_data_frame(tweets)
tweets_df['tweets'] = pd.DataFrame([tweet_collector.clean_tweet(tweet) for tweet in tweets_df['tweets']])
tweets_df = tweets_df.drop_duplicates(subset=['tweets'])
tweets_df['sentiment'] = np.array([tweet_collector.analyze_sentiment(tweet) for tweet in tweets_df['tweets']])

#[print(tweet, sent) for tweet, sent in zip(tweets_df['tweets'][:30], tweets_df['sentiment'][:30])]

