import boto3
client  = boto3.client('s3')

client.upload_file('hello.txt', 'boto-bucket-test1989', 'hello.txt')
client.upload_file('hello2.txt', 'boto-bucket-test1989', 'hello2.txt')
client.upload_file('hello3.txt', 'boto-bucket-test1989', 'hello3.txt')