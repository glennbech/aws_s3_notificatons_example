import json
import csv
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        response = s3.get_object(Bucket=bucket, Key=key)
        lines = response['Body'].read().decode('utf-8').splitlines()
        reader = csv.DictReader(lines)
        rows = list(reader)

        json_key = key.replace('.csv', '.json')
        s3.put_object(Bucket=bucket, Key=json_key, Body=json.dumps(rows))

    return {
        'statusCode': 200,
        'body': json.dumps('CSV to JSON conversion successful')
    }
