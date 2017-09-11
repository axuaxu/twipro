import boto3
import datetime

print datetime.datetime.now()


# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put an event rule   "cron(0 20 * * ? *)"
response = cloudwatch_events.put_rule(
    Name='TWI_EVENT',
    RoleArn='arn:aws:iam::969340917686:role/axevent1',
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED'
)

# Put target for rule
response = cloudwatch_events.put_targets(
    Rule='TWI_EVENT',
    Targets=[
        {
            'Arn': 'arn:aws:lambda:us-east-1:969340917686:function:twi_img',
            'Id': 'myCloudWatchEventsTarget',
        }
    ]
)
print(response)

#print(response['RuleArn'])
