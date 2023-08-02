import boto3
client  = boto3.client('s3')


response = client.create_bucket(
    Bucket='boto-bucket-test1989'
)

print(response['Location'])

