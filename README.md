# Control RaspberryPi GPIO using Amazon Simple Queue Service SQS
Code snippets for SQS operations and S3 operations using Boto3 library. Example of controlling LED (Turn ON and OFF) in a Raspberrypi board using AWS SQS service remotely. 

# Requirements -->
pip install python-decouple
pip install boto3
pip install RPi.GPIO

# File download 
Example code will download a file only if it is not present in a local folder. If same name file is present in local folder, it compares the filesizes in both locations. If not present or mismatch, it will download the file.

# Send, receive, delete SQS message 
Perform SQS opeartions. Example creates queues with the name as The MAC address of the device. 
