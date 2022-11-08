import boto3
from boto3.dynamodb.conditions import Key, Attr


class SkillDAO:

    def __init__(self):
        pass

    def getSkill(self, id):
        client = boto3.resource('dynamodb')

        table = client.Table('skill_table')

        response = table.scan(
            FilterExpression=Attr('id').eq(id)
        )
        item = response["Items"][0]
        return item
