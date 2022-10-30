import boto3

# Pseudo code
kendra = boto3.client("kendra")


def refresh_index(event, context):
    print(event)
