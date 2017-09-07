import tweepy
consumer_key='rD7LSDlI4TF3Iw1p9Q9xQ3lCh'
consumer_secret ='pMvAJIUAxMzDyZjKEqHSo1k7qEHyo4sHmYTdEmAWTDplq4Zkfu'
access_token= '899308310461075457-LxqERAtAfzgWbXHjT1k65MDsntNgxqz'
access_token_secret= 'IMz3fbb0eop316Wid7JaHvLSfNnzcqRiv4Et9qlv5F56M'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get all the people the user follows
friends = api.friends_ids()

# Print out each one
for id in friends:
    print(id)

friendsFile = open("friends.txt","w")

for id in friends:
    friendsFile.write(str(id) + "\n")

friendsFile.close()
