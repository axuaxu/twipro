import boto3
from boto3.dynamodb.conditions import Key, Attr
from random import randint

import os
import tweepy
from credentials import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

s3 = boto3.resource('s3')

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('imglist')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
#print(table.creation_date_time)
#f= open('imglist.txt','r')
#for line in f:
#  table.put_item(
#     Item={
#        'name': line,
#        }
#      )
#response = table.get_item(
#    Key={
#        'name': 'janedoe',
#    }
#)
#item = response['Item']
#print(item)

response = table.scan(
    FilterExpression=Attr('name').begins_with('images')
)
#items = response['Items'][0]
#print(items)
count = len(response['Items'])
i = randint(0,count)
print i
item  =  response['Items'][i]
print(item['name'])
nstr =  item['name'].encode('utf-8').replace('\n','')
narr = nstr.split('/')
print(len(narr))
if  len(narr)==3:
    painter = narr[1]
    pic = narr[2]
    pic=  pic.split('.')[0]
    painter = painter.replace('-',' ')
    pic = pic.replace('-',' ')
    print (painter)
    print (pic)
    status =  painter+'\n'+pic
    status = status.title()
    myb = "axufile"
    tmpf = '/tmp/'+narr[2]
    print(myb,nstr,tmpf)
    boto3.client('s3').download_file(myb,nstr,tmpf)
    file = open(tmpf,'rb')
    api.update_with_media(tmpf, status=status)
    table.delete_item(
         Key={
           'name': item['name'],
       })
