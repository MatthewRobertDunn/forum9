#!/usr/bin/env python
import boto3
from config import QUEUE_URL
from request_handler import handle_request

def submit(body):
    # Initialize the SQS client
    sqs = boto3.client('sqs')
    # Ensure the 'message' field exists, otherwise raise a ValueError
    if 'message' not in body:
        raise ValueError("'message' field is required in the input")

    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        # Convert the dictionary to a JSON string
        MessageBody=body['message'].strip()
    )
    # Print the response
    return response['MessageId']