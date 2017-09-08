import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('axufile')
for key in bucket.objects.all():
    if key.key.startswith('images'):
       print(key.key)
    #name = key.key
    #if  name.startswith('images'):
    #    print name

