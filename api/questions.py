#!/usr/bin/env python
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime, timezone
from config import TABLE_NAME
from request_handler import handle_request
def handle(year = None, **kwargs):
    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    # Query the table
    try:
        year = int(year)
    except:
        year = datetime.now(timezone.utc).year

    response = table.query(
         IndexName="year-created_date-index",
        KeyConditionExpression=Key('year').eq(year),
        ProjectionExpression='id, question, created_date',
        ScanIndexForward=False,  # False to order by descending,
    )

    # Extract the items from the response
    items = response.get('Items', [])
    return items
    

#Entry point
if __name__ == "__main__":
    handle_request(handle, 'GET')  # Call handle_request and pass the service function