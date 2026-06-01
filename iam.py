import boto3

def IAM_users(event, context):

    client = boto3.client('iam')

    response = client.list_users()

    print("****************************************************************")
    print(type(response))
    print(response)
    print("****************************************************************")
    print(response.keys())
    print("****************************************************************")
    print(type(response['Users']))
    print(response['Users'])
    print("****************************************************************")
    print(type(response['Users'][0]))
    print((response['Users'][0]))
    print("****************************************************************")
    print(type(response['Users'][0]['UserName']))
    print((response['Users'][0]['UserName']))

    return {
        'statusCode': 200
    }
