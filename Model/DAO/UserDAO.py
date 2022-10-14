import boto3
from boto3.dynamodb.conditions import Key, Attr


class UserDAO:

    def __init__(self):
        pass

    def add_user(self, user):
        client = boto3.resource('dynamodb')

        table = client.Table('user_table')

        response = table.put_item(

            Item={

                'id': user["id"],

                'username': user['username'],

                'first_name': user['first_name'],

                'last_name': user['last_name'],

                'password': user['password'],

                'profile_pic_URL': user['profile_pic_URL'],

                'current_module': user['current_module'],

                'current_streak': user['current_streak']

            }

        )

        return True

    def get_user(self, username, password):
        client = boto3.resource('dynamodb')

        table = client.Table('user_table')

        response = table.scan(
            FilterExpression=Attr('username').eq(username)
        )
        item = response["Items"][0]
        return item
