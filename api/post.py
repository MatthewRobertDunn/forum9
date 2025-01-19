#!/usr/bin/env python
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime, timezone
from config import TABLE_NAME
from request_handler import handle_request
def handle(id, **kwargs):
    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    # Query the table
    response = table.query(
        KeyConditionExpression=Key('id').eq(id),
    )

    # Extract the items from the response
    items = response.get('Items', None)
    return items[0] if items else None
    

#Entry point
if __name__ == "__main__":
    handle_request(handle, 'GET')  # Call handle_request and pass the service function