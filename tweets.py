import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "la9DXR776NLHeDmnNayy14kyb"
# api secret key
api_secret_key = "mA4BbYbhZZ5bx5sYjcqQ4g3fWDTscwKTLQrjWEdzYRHps1MBiy"
# access token
access_token = "1309782130780762112-bylPtb3WCbnJIDLe78o25ysSm42mtq"
# access token secret
access_token_secret = "LWr2j7PPXgWSaFVeB2XMlr5qUPOuGff3c2uQGg3DnCNVK"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 50
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)