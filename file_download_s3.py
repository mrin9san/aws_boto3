# Check for a particular file in a local folder, if not present, download it from S3 bucket
import boto3
import os
import time
from decouple import config
# Pick variables
akey=config('AKEY')
skey=config('SKEY')
region=config('REGION')
# Declare Boto objects
s3_client = boto3.client("s3",aws_access_key_id=akey,aws_secret_access_key=skey)
s3_resource = boto3.resource('s3',aws_access_key_id=akey,aws_secret_access_key=skey)

# Choosing current directory to upload file
file_path=os.getcwd()
filename="vid1.mp4"

# Print out bucket names
    for bucket in s3_resource.buckets.all():
        print(bucket.name)
      
 # Upload the file      
s32.upload_file(
   Filename=os.path.join(file_path,filename),
   Bucket="Bucket_1",
   Key=filename)
# Provide list of filenames to be checked
list1=["vid.mp4","vid2.mp4"]

file_path_download="/Give a path/"
object_name='give the object name'
for i in list1: 
    f = i
    while file_path != "/" and f not in os.listdir(file_path):
        file_path_download = os.path.abspath(file_path_download + "/../")

    if os.path.isfile(os.path.join(file_path_download,f)):
        print("Accessing file - %s" %i)
        object = s3.Object(object_name,i)
        file_size = object.content_length 
        if file_size==os.path.getsize(os.path.join(d,f)):
            print("I found a same file name as {}. So comapring the file sizes..".format(i))
            print("Found {} in local directory. So I am not downloading it.".format(i))  
    else:
        print("{} is a new file, so downloading it..".format(i))
        s3_client.download_file(object_name, i ,"{}/{}".format(file_path,i))
