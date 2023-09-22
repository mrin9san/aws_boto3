import boto3
import json
from decouple import config

akey=config('AKEY')
skey=config('SKEY')
region=config('REGION')

# Find the MAC addres of the device 
from getmac import get_mac_address as gma
#print(gma())

# Declare SQS client
sqs_client = boto3.client("sqs",aws_access_key_id=akey,aws_secret_access_key=skey,region_name=region)

# Create a SQS queue
response_create_queue = sqs_client.create_queue(
    QueueName='SQS_client_MAC_list',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)

response_list_queue = sqs_client.list_queues()

print("Response 2 is important",response_list_queue['QueueUrls'])
print(response['QueueUrl'])

queue_url = response_create_queue['QueueUrl']

# Send message to SQS queue
response1 = sqs_client.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about my device'
    )
)

#print(response1['MessageId'])

