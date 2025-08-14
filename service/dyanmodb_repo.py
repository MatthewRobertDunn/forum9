import boto3
from config import TABLE_NAME


def insert_discussion(post):
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=post)
    print("Item inserted successfully!")


def get_discussion(id):
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={'id': id})
    return response['Item']
