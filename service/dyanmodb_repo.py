import boto3
from config import TABLE_NAME


def insert_thread(thread):
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=thread)
    print("Item inserted successfully!")


def get_thread(id):
    # Initialize the DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)
    response = table.get_item(Key={'id': id})
    return response['Item']
