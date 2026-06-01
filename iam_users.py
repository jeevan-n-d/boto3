import boto3

def IAM_users(event, context):

    client = boto3.client('iam')

    response = client.list_users()

    for user in response['Users']:
        print(user['UserName'])

    return {
        'statusCode': 200
    }
