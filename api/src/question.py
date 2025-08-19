from boto3.dynamodb.conditions import Key
from request_handler import handle_request
from dynamodb import table

def question(id: str):
    # Query the table
    response = table.query(
        KeyConditionExpression=Key('id').eq(id),
    )

    # Extract the items from the response
    items = response.get('Items', None)
    return items[0] if items else {}