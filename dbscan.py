#!/usr/bin/env python3.5

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

s3client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb', region_name='us-west-1')

table_name = 'msri-video-tube'
s3_bucket = 'msri-video-tube-source-bbwudbcpp32z'

table = dynamodb.Table(table_name)

def delete_items(item):
    for i in item:
        try:
            response = table.delete_item(TableName=table_name,Key={'guid': i['guid']})
            print("Deleting rows from DB with guid: %s with workflowStatus as %s and name is %s" % (i['guid'], i['workflowStatus'], i['newVideoName']))
            if i['workflowStatus'] == 'error':
                print("Deleting file from Source S3 with name %s" % i['newVideoName'])
                s3client.delete_object(Bucket=s3_bucket, Key=i['newVideoName'])
        except ClientError as e:
            print('Something is wrong while deleting item')
            print("Delete Response is : ", e.response['Error']['Message'])


fe = Attr('workflowStatus').eq('complete') | Attr('workflowStatus').eq('error')
pe = "guid, workflowStatus, origVideoName, newVideoName"

try:
    first_scan = table.scan(FilterExpression=fe,ProjectionExpression=pe)
    # print(json.dumps(first_scan,indent=2))
    if first_scan['Count'] == 0:
        print("No rows to delete")
    else:
        delete_items(first_scan['Items'])

except ClientError as e:
    print("Found issues while scanning DyanmoDB ->", e.response['Error']['Message'])

while 'LastEvaluatedKey' in first_scan:
    try:
        response = table.scan(ProjectionExpression=pe,FilterExpression=fe,ExclusiveStartKey=first_scan['LastEvaluatedKey'])
        if  response['Count'] == 0:
            print("No rows to be deleted")
        else:
            delete_items(response['Items'])
    except ClientError as e:
        print("Found issues while scanning DyanmoDB ->", e.response['Error']['Message'])
