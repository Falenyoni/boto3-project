import boto3
client  = boto3.client('ec2')

response = client.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available',
            ]
        }
    ]
)

for volume in response['Volumes']:
    print(volume['VolumeId'], volume['Size'])
    response = client.delete_volume(
    VolumeId=volume['VolumeId']
    )