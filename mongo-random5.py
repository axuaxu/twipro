#http://api.mongodb.com/python/current/index.html
#https://www.mongodb.com/blog/post/how-to-perform-random-queries-on-mongodb
#http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_connecting_accessing.php
#https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
from pymongo import MongoClient
import datetime
import requests
import os
import tweepy
from time import sleep
from credentials import *


client = MongoClient("mongodb://localhost:27017")
db = client.flist
coll = db.flist
 
#print(coll.find_one())
#print(db.version)
#db.coll.aggregate([{$sample: {size: 1}}])
winner = [ d for d in coll.aggregate([{'$sample': {'size': 1 }}])][0]
print(winner)
print(winner['_id'])


now = datetime.datetime.utcnow()
print (now)

id = winner['_id']
coll.update_one(
	{"_id":id},
	{"$set":{"twi":"x"},
	 "$currentDate": {"lastModified": True}})
	
#coll.delete_one({"_id":id})

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



#url = "http://media02.hongkiat.com/raspberry-pi-projects/1-lappi-netbook.jpg"
#fn = ".\img\paul-cezanne\pierrot-and-harlequin-mardi-gras-1888.jpg"
#message = "landscape"
#tweet_image(url,message)
fn = winner['dir']+'\\'+winner['name']
#message = ''
print (fn)
painter = winner['dir'].split('\\')[2].replace('-',' ')
pname = winner['name'].split('.')[0].replace('-',' ')
message = painter.title()+'\n'+pname.title()
#print (painter)
#print (pname)
print(message)
api.update_with_media(fn, status=message)

coll.delete_one({"_id":id})
