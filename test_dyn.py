import boto3
from boto3.dynamodb.conditions import Key, Attr

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
items = response['Items'][10]
print(items)
print(len(response['Items']))
