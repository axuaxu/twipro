#https://spin.atomicobject.com/2014/09/24/automate-amazon-s3-python/
#https://spin.atomicobject.com/2014/09/24/automate-amazon-s3-python/
import boto3
s3 = boto3.resource('s3')
boto3.client('s3').list_buckets()
boto3.client('iam').list_users()

for bucket in s3.buckets.all():
        print(bucket.name)
#        for object in  bucket.objects.all():
#           print(object)
#conn = S3Connection()
#        for file_key in bucket:
#            print file_key.name
tmpf = '/tmp/{}.jpg'
boto3.client('s3').download_file('axufile','images/emile-claus/hay-stacks-1905.jpg',tmpf)
