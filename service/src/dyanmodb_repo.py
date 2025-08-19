import boto3
from .config import TABLE_NAME


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
    return response.get('Item')


def append_post(id: str, new_post: dict[str, str]):
    """
    Append a single post to the 'posts' list in a thread.
    new_post should be a dict like {'content': '...', 'persona': '...'}
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    table.update_item(
        Key={'id': id},
        UpdateExpression='SET post = list_append(if_not_exists(post, :empty_list), :new_post)',
        ExpressionAttributeValues={
            ':new_post': [new_post],  # Pass as a list for list_append
            ':empty_list': []          # Ensures posts exists if empty
        }
    )
    print(f"Appended new post to thread {id}")


def remove_is_processing(id: str):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    table.update_item(
        Key={'id': id},
        UpdateExpression='REMOVE is_processing'
    )
