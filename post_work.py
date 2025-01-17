#!/usr/bin/env python
import boto3
from config import QUEUE_URL
from request_handler import handle_request

def post_work(request):
    # Initialize the SQS client
    sqs = boto3.client('sqs')
    # Ensure the 'message' field exists, otherwise raise a ValueError
    if 'message' not in request:
        raise ValueError("'message' field is required in the input")
    
    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=request['message']  # Convert the dictionary to a JSON string
    )
    # Print the response
    return response['MessageId']

#Entry point
if __name__ == "__main__":
    handle_request(post_work)  # Call handle_request and pass the service function