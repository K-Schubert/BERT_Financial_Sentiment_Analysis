# BERT_Financial_Sentiment_Analysis

# Summary
Using Tweepy to pull data from Twitter (code inspired from LucidProgramming's repo: https://github.com/vprusso/youtube_tutorials/tree/master/twitter_python) and using BERT to predict daily sentiment for stocks. The idea is to create a model where daily sentiment can be used as a predictor for stock price movement. Then add relevant news sources and have a sentiment index for "politics", "financial", etc.

# Current Progress
At the moment, using ~450'000 reviews from ~500 apps from the Google Play store to fine-tune BERT. The "star rating" of an app is useful as it allows to assign a sentiment to the review to train the model. Then will use this model on Twitter data.

# Training

## Round 1
Trained BERT model_2 on 450'000 Google Play reviews from 500 apps of all categories (Art & Design, Beauty, etc.). Trained for 10 epochs (17 hrs) on a single GPU to achieve 75% test accuracy. This is worse than model_1 (84% test acc) trained for 10 epochs (1 hr) on 15'000 reviews. However, the issue of val loss increasing with val acc has been resolved and is probably due to the increase in the val dataset size. For the next round of training, will train model_1 for more epochs on the small dataset and compare to training model_2 on the larger dataset for the same number of epochs while resorting to using at least 4 GPUs this time.

## Round 2

# Twitter Data
Need to decide what strategy to adopt. First will try targeting a single stock, pull tweets with the appropriate hashtag and build the stock prediction model. Then will try to broaden the scope and target an index using tweets from its components (e.g. NASDAQ -> APPL, GOOG, etc.). Finally will try to build sentiment indexes for the political mood, economic mood, etc.
