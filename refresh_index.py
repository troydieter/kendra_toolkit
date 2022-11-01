import boto3
from botocore.exceptions import ClientError

# Establish the Amazon Kendra Client
kendra = boto3.client("kendra")

# Set the Amazon Kendra Index
INDEX_NAME = 'example'

try:
    response = kendra.list_data_sources(
        IndexId=INDEX_NAME,
        MaxResults=10
    )

except  ClientError as e:
        print("%s" % e)
