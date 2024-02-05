import json
import boto3

def lambda_handler(event , context):
    #Create Kinesis Client
    kinesis_client = boto3.client('kinesis')
    #Iterate through records in the event

    for records in event['Records']:
        #Process the data
        input_data = json.loads(record['kinesis']['data'])     
