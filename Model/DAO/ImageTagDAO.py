import boto3
from boto3.dynamodb.conditions import Key, Attr


class ImageTagDAO:

    def __init__(self):
        pass

    def get_image_tags(self):
        client = boto3.resource('dynamodb')
        table = client.Table('image_tags_table')
        response = table.get_item(Key={"tags": "tags"})
        return response["Item"]