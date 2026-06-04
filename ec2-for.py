import boto3

from pprint import pprint

def ec2(event, context):

    client = boto3.client('ec2')
    
    res=client.describe_instances()

    #print(res['Reservations'][0]['Instances'][0]['InstanceId'])

    sam=res['Reservations']

    for re in sam:
        for inst in re['Instances']:
            print(inst['InstanceId'])
