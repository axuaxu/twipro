import datetime
from random import randint

now = datetime.datetime.now()
hour = now.hour
print (now)
print (now.hour,now.minute)

tin = randint(30,60)
if  (3<= now.hour <=9):
      tin = randint(60,120)
      
print(tin) 
