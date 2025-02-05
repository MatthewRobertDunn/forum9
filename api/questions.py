#!/usr/bin/env python
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime, timezone
from config import TABLE_NAME
from request_handler import handle_request
from datetime import datetime
def handle(date: str = None, **kwargs):
    # Initialize a session using Amazon DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    # Query the table
    parsed_date = None

    if date is not None:
        if date.endswith('Z'):
            date = date[:-1] + '+00:00'

    try:
        parsed_date = datetime.fromisoformat(date)
    except:
        parsed_date = datetime.now(timezone.utc)

    response = table.query(
        IndexName="year-created_date-index",
        KeyConditionExpression=Key('year').eq(parsed_date.year) & Key('created_date').lt(parsed_date.isoformat()),
        ProjectionExpression='id, question, created_date',
        ScanIndexForward=False,  # False to order by descending,
        Limit=20
    )

    # Extract the items from the response
    items = response.get('Items', [])
    return items
    

#Entry point
if __name__ == "__main__":
    handle_request(handle, 'GET')  # Call handle_request and pass the service function