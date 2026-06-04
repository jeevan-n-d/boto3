import boto3

from pprint import pprint

def ec2(event, context):

    client = boto3.client('ec2')
    
    res=client.describe_instances()

    #print(res['Reservations'][0]['Instances'][0]['InstanceId'])

    sam=res['Reservations'][2]['Instances']

    for id in sam:
        print(id['InstanceId'])
