#!/usr/bin/env python
import boto3
from config import QUEUE_URL
from request_handler import handle_request

def post_work(body, **kwargs):
    # Initialize the SQS client
    sqs = boto3.client('sqs')
    # Ensure the 'message' field exists, otherwise raise a ValueError
    if 'message' not in body:
        raise ValueError("'message' field is required in the input")
    
    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=body['message'].trim()  # Convert the dictionary to a JSON string
    )
    # Print the response
    return response['MessageId']

#Entry point
if __name__ == "__main__":
    handle_request(post_work, 'POST')  # Call handle_request and pass the service function