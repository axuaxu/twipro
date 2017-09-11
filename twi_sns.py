import boto3

sns = boto3.client('sns')

response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:969340917686:twi',
    Message='aws twitter',
    Subject='aws lambda twit 01'
)
