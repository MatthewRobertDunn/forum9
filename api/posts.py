#!/usr/bin/env python
import boto3
from config import QUEUE_URL
from request_handler import handle_request

def handle(**kwargs):
    # Initialize the SQS client
    

#Entry point
if __name__ == "__main__":
    handle_request(handle, 'GET')  # Call handle_request and pass the service function