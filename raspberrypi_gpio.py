import RPi.GPIO as GPIO
import boto3
import json
import time
from decouple import config

akey=config('AKEY')
skey=config('SKEY')
region=config('REGION')

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD) # use Physical GPIO Numbering,
    GPIO.setup(ledPin, GPIO.OUT) # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW) # make ledPin output LOW level
    print ('using pin%d'%ledPin)


def turn_on():
    GPIO.output(ledPin, GPIO.HIGH)
    print ('led turned on >>>')


def turn_off():
    GPIO.output(ledPin, GPIO.LOW)
    print ('led turned off >>>')


def destroy():
    GPIO.cleanup()
    

while True:
    time.sleep(5)
    setup()
    sqs_client = boto3.client("sqs",aws_access_key_id=akey,aws_secret_access_key=skey,region_name=region)
    queue='give queue url'

    while(True):
        response = sqs_client.receive_message(
        QueueUrl=queue,
        AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=10,
        MessageAttributeNames=['All'],
        VisibilityTimeout=2,
        WaitTimeSeconds=5
        )
                    # message = response['Messages'][0]
                    # print(message)
        message=response.get("Messages")
        if len(response.get('Messages', [])) !=0:            
            message_body = message[0]["Body"]
            if message_body=='turn_on':
                turn_on()
            if message_body=='turn_off':
                turn_off()       	
            sqs_client.delete_message(QueueUrl=queue, ReceiptHandle=response['Messages'][0]["ReceiptHandle"]) 
        if len(response.get('Messages', [])) ==0:
            break
