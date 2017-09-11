import boto3
from random import randint
import datetime

def lamb_sns(event,context):
  sns = boto3.client('sns')

  response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:969340917686:test',
    Message='aws test',
    Subject='aws test topic'
     )

  now = datetime.datetime.now() 
  hour = now.hour
  print (now)
  print (now.hour,now.minute)

  tin = randint(3,6)
  if  (3<= now.hour <=9):
      tin = randint(6,12)

  print(tin)

  ratestr = 'rate('+tin+' minutes)'
  print ratestr

  # Create CloudWatchEvents client
  cloudwatch_events = boto3.client('events')

  # Put an event rule
  response = cloudwatch_events.put_rule(
    Name='TEST_EVENT',
    RoleArn='arn:aws:iam::969340917686:role/axevent1',
    ScheduleExpression=ratestr,
    State='ENABLED'
   )
  print(response['RuleArn'])
# Put target for rule
  response = cloudwatch_events.put_targets(
    Rule='TEST_EVENT',
    Targets=[
        {
            'Arn': 'LAMBDA_FUNCTION_ARN',
            'Id': 'myCloudWatchEventsTarget',
        }
     ]
  )
  print(response)

