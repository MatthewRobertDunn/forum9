from config import TABLE_NAME
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)