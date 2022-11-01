import boto3
from botocore.exceptions import ClientError

# Establish the Amazon Kendra Client
kendra = boto3.client("kendra")

# Set the Amazon Kendra Index
INDEX_ID = 'XX'

try:
    response = kendra.list_data_sources(
        IndexId=INDEX_ID,
        MaxResults=10
    )
    print(response)

except  ClientError as e:
        print("%s" % e)
