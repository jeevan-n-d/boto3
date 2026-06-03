import boto3

from pprint import pprint

def IAM_users(event, context):

    aws_man = boto3.session.Session()

    aws_management_client = boto3.client('iam')

    response = aws_management_client.list_users()

    pprint(response)

    for users in response['Users']:
        print(users['UserName'])
