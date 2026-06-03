import boto3

def IAM_users(event, context):

    aws_resource = boto3.session.Session()

    resource=aws_resource.resource('iam')

    for user in resource.users.all():
        print(user.name)

    
    aws_management_client = boto3.client('iam')

    response =  aws_management_client.list_users()

    print(response)

    print("****************************")
    
    print(response['Users'])

    print("****************************")

    print(response['Users'][0])

    print("****************************")

    print(response['Users'][0]['UserName'])


    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")
    print("****************************")

    for users in response['Users']:
       print(users['UserName'])
