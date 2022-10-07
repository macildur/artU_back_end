import boto3
import uuid


def add_user(event):
    client = boto3.resource('dynamodb')

    table = client.Table('user_table')

    response = table.put_item(

        Item={

            'id': str(uuid.uuid4()),

            'username': event['username'],

            'first_name': event['first_name'],

            'last_name': event['last_name'],

            'password': event['password'],

            'profile_pic_URL': event['profile_pic_URL'],

            'current_module': event['current_module'],

            'current_streak': event['current_streak']

        }

    )

    return {

        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

        'body': 'Record ' + event['username'] + ' added'

    }