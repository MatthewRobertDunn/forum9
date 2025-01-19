#!/usr/bin/env python
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime, timezone
from config import TABLE_NAME
from request_handler import handle_request
def handle(year = None, **kwargs):
    return {"message": "pong"}
    

#Entry point
if __name__ == "__main__":
    handle_request(handle, 'GET')  # Call handle_request and pass the service function