#!/usr/bin/env python3.5

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
# import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

client = boto3.client('dynamodb')

table_name = 'msri-video-tube'

dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
table = dynamodb.Table(table_name)

def print_resp(item):
    for i in item:
        try:
            print("guid is " + i['guid'] + 'and workflowStatus is ' + i['workflowStatus'])
        except:
            print("Something is wrong")
            raise


# def check_s3(item):
#     for i in item:
#         try:
#             response = s3client.head_object(Bucket=s3_bucket, Key=i['newVideoName'])
#             print(json.dumps(response, indent=4, sort_keys=True, default=str))
#         except ClientError as e:
#             print('Unable to locate ' + i['newVideoName'] + ' in s3 bucket ' + s3_bucket)
#             print(e.response)

# def delete_s3_file(item):
#     for i in item:
#         try:
#             response = s3client.delete_object(Bucket=s3_bucket, Key=i['newVideoName'])
#             print(json.dumps(response, indent=4, sort_keys=True, default=str))
#         except ClientError as e:
#             print('Unable to locate ' + i['newVideoName'] + ' in s3 bucket ' + s3_bucket)
#             print(e.response)



def delete_rows(item):
    for i in item:
        try:
            response = table.delete_item(
                TableName=table_name,
                Key={'guid': i['guid']}
            )
            print("Delete Response is : ", response)
        except:
            raise Exception('Something is wrong while deleting item')


def delete_rows_client(item):
    for i in item:
        resp = client.delete_item(
            TableName=table_name,
            Key={
            'guid': { 'S' : i['guid']}
            }
        )
        print("Deleting ", i['guid'])
        print("Delete respose of ", i['guid'])
        print(resp)


# dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
# table = dynamodb.Table('msri-video-tube')

fe = Attr('workflowStatus').eq('complete') | Attr('workflowStatus').eq('error')
pe = "guid, workflowStatus"
# Expression Attribute Names for Projection Expression only.
# ean = { "#uid": "guid", }
# esk = None

try:
    response = table.scan(
        FilterExpression=fe,
        ProjectionExpression=pe,
        # ExpressionAttributeNames=ean,
        # Limit=5
        )

    print_resp(response['Items'])

    # delete_rows(response['Items'])
    # delete_rows_client(response['Items'])

except (ClientError) as e:
    if e.response['Error']['Code'] == "ResourceNotFoundException":
        print("Provided resource not found. Check the resouce exists")
        print(e.response['Error']['Message'])
except:
    print("Something is wrong. Check exception")
    raise


# print_resp(response['Items'])
# for i in response['Items']:
#     print(json.dumps(i, cls=DecimalEncoder))

# while 'LastEvaluatedKey' in response:
#     response = table.scan(
#         ProjectionExpression=pe,
#         FilterExpression=fe,
#         ExpressionAttributeNames= ean,
#         ExclusiveStartKey=response['LastEvaluatedKey']
#         )
#
#     for i in response['Items']:
#         print(json.dumps(i, cls=DecimalEncoder))
