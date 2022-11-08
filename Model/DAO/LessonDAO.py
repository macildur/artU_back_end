import boto3
from boto3.dynamodb.conditions import Key, Attr


class LessonDAO:

    def __init__(self):
        pass

    def getLesson(self, id):
        client = boto3.resource('dynamodb')

        table = client.Table('lesson_table')

        response = table.scan(
            FilterExpression=Attr('id').eq(id)
        )
        item = response["Items"][0]
        return item
