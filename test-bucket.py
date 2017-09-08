#https://boto3.readthedocs.io/en/latest/guide/migrations3.html#iteration-of-buckets-and-keys
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)

#for bucket in s3.buckets.all():
#    for key in bucket.objects.all():
#        print(key.key)
