import boto3
from botocore.exceptions import ClientError

def insert_post(post):
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    # Replace with your table name
    table_name = 'forum9'
    # Reference your DynamoDB table
    table = dynamodb.Table(table_name)
    table.put_item(Item=post)
    print("Item inserted successfully!")
