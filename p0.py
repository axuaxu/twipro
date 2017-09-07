import boto3
s3 = boto3.resource('s3')
boto3.client('s3').list_buckets()
boto3.client('iam').list_users()
for bucket in s3.buckets.all():
        print(bucket.name)
