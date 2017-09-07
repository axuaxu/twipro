import tweepy
consumer_key='rD7LSDlI4TF3Iw1p9Q9xQ3lCh'
consumer_secret ='pMvAJIUAxMzDyZjKEqHSo1k7qEHyo4sHmYTdEmAWTDplq4Zkfu'
access_token= '899308310461075457-LxqERAtAfzgWbXHjT1k65MDsntNgxqz'
access_token_secret= 'IMz3fbb0eop316Wid7JaHvLSfNnzcqRiv4Et9qlv5F56M'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
