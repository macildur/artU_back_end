import boto3
from boto3.dynamodb.conditions import Key, Attr


class SkillDAO:

    def __init__(self):
        pass

    def getMatchingImages(self, requested_attrs):
        primary_category = requested_attrs["primary_category"]
        secondary_categories = requested_attrs["secondary_categories"]
        client = boto3.resource('dynamodb')

        table = client.Table('skill_table')
        response = None
        print("len_sec ", len(secondary_categories), "\n", secondary_categories)
        if len(secondary_categories) == 2:
            response = table.scan(
                FilterExpression=Attr('primary_category').eq(primary_category) & (
                            Attr("secondary_categories").eq(secondary_categories[0]) | Attr("secondary_categories").eq(
                        secondary_categories[1]))
            )
        elif len(secondary_categories) == 1:
            response = table.scan(
                FilterExpression=Attr('primary_category').eq(primary_category) & Attr("secondary_categories").eq(
                    secondary_categories[0])
            )

        items = response["Items"]

        return {
            'statusCode': 200,
            'body': items
        }
