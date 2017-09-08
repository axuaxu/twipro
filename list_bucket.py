import boto3

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

s3 = boto3.resource('s3')
bucket = s3.Bucket('axufile')
t=''
for key in bucket.objects.all():
    if key.key.startswith('images'):
       #print(key.key)
       t = t+ key.key +'\n'
print t
    #name = key.key
    #if  name.startswith('images'):
    #    print name

f = open('imglist.txt', 'w')
f.write(t)
f.close()
