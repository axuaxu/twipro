import boto3
import datetime

print datetime.datetime.now()


# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put an event rule   "cron(0 20 * * ? *)"
response = cloudwatch_events.put_rule(
    Name='DEMO_EVENT',
    RoleArn='arn:aws:iam::969340917686:role/axevent1',
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED'
)

# Put target for rule
response = cloudwatch_events.put_targets(
    Rule='DEMO_EVENT',
    Targets=[
        {
            'Arn': 'LAMBDA_FUNCTION_ARN',
            'Id': 'myCloudWatchEventsTarget',
        }
    ]
)
print(response)

print(response['RuleArn'])
