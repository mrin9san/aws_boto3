import boto3
import json
from decouple import config

# Pick env variables
akey=config('AKEY')
skey=config('SKEY')
region=config('REGION')

# Declare boto client
sqs_client = boto3.client("sqs",aws_access_key_id=akey,aws_secret_access_key=skey,region_name=region)
queue_url='provide the queue url here'
queue=queue_url

# Receive message
response = sqs_client.receive_message(
QueueUrl=queue,
AttributeNames=[
    'SentTimestamp'
],
MaxNumberOfMessages=10,
 MessageAttributeNames=[
'All'],
VisibilityTimeout=0,
WaitTimeSeconds=10
)
message=response.get("Messages")

#print(message)
message_body = message[0]["Body"]
print(message_body)
#print(f"Message body: {json.loads(message_body)}")

#Delete message
for msg in response['Messages']:
    if len(response.get('Messages', [])) !=0:
        delete_message= sqs_client.delete_message(QueueUrl=queue, ReceiptHandle=msg["ReceiptHandle"]) 
    print('delete_message', delete_message)
    if len(response.get('Messages', [])) == 0:
        print("No messages to delete")
        break
