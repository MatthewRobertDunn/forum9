import boto3
from botocore.exceptions import ClientError
from config import TABLE_NAME
def insert_post(post):
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    # Replace with your table name
    # Reference your DynamoDB table
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=post)
    print("Item inserted successfully!")
