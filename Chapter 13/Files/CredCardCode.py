import boto3
client = boto3.client('s3')
import json
from botocore.config import Config
from boto3.s3.transfer import TransferConfig


config={"region":"af-south-1",
        "key_id": "AKIAQSPFTRNERKWJ437U",
        "s_key" :"rNW0gKhauin7tH+/DN5A04PPmKy/oQ/mpwk6TfnN",
        "key_id2": "AKIAQSPFTRNEWA2IQ7HR",
        "s_key2":"iGuA4LemekKg5mp0MigNcKO1kSHKp3HRa6DdM/GI",
        "bucket_1": "S3://internal-audit-za"}


aws_config = Config(
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    },
    connect_timeout = 1300,
    region_name = config['region']
)

aw_config = Config(connect_timeout=3400, read_timeout=2400, region_name=config['region'])

cnx = boto3.client("s3", aws_access_key_id=config['key_id'], aws_secret_access_key=config['s_key'], config=aw_config)


s3 = boto3.resource('s3')

bucket = s3.Bucket("internalaudit-za-sftp")


#print(bucket.objects.all())

files =[]

for obj in bucket.objects.all():
    if obj.key[:19]=='traderoot/EOH MTH/[':
       # print(obj.key)
        files.append(obj.key)

print(files[1])

