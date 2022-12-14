import boto3
from boto3.dynamodb.conditions import Key, Attr


class SkillDAO:

    def __init__(self):
        pass

    def getMatchingImages(self, requested_attrs):
        attrs = []
        for tag in ("primary_category", "secondary_category", "tertiary_category"):
            cur_attr = requested_attrs[tag]
            if cur_attr == "":
                if tag != "tertiary_category":
                    return f"Error: \'{tag}\' not selected. \'{tag}\' must be specified in order to search the database"
                else:
                    continue
            attrs.append(Attr(tag).eq(cur_attr))

        fe = attrs[0]
        for i in range(1, len(attrs)):
            fe = fe & attrs[i]

        client = boto3.resource('dynamodb')
        table = client.Table('skill_table')
        response = table.scan(
            FilterExpression=fe
        )

        items = response["Items"]
        items = [d["url"] for d in items]

        return items
