#!/usr/bin/env python
from boto3.dynamodb.conditions import Key
from datetime import datetime, timezone
from request_handler import handle_request
from datetime import datetime
from dynamodb import table

def questions(date: str = None, reverse = None, **kwargs):  
    # Convert the date string to a datetime object
    # and set a default value
    if date is not None:
        if date.endswith('Z'):
            date = date[:-1] + '+00:00'

    parsed_date = None
    try:
        parsed_date = datetime.fromisoformat(date)
    except:
        parsed_date = datetime.now(timezone.utc)

    iso_date = parsed_date.isoformat()

    #default sort order is to get posts earlier than given date, unless reverse is requested
    sort_by = Key('created_date').gt(iso_date) if reverse else Key('created_date').lt(iso_date)

    response = table.query(
        IndexName="year-created_date-index",
        KeyConditionExpression=Key('year').eq(parsed_date.year) & sort_by,
        ProjectionExpression='id, question, created_date',
        ScanIndexForward=True if reverse else False,  # False to order by descending,
        Limit=20
    )

    # Extract the items from the response
    items = response.get('Items', [])
    return items
  

#Entry point for CGI version
if __name__ == "__main__":
    handle_request(questions, 'GET')  # Call handle_request and pass the service function