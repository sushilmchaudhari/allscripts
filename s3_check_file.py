#!/usr/bin/env python3.5

from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

# s3client = boto3.client('s3')

s3_bucket = 'msri-video-tube-source-bbwudbcpp32z'
key = '002385d5-a363-4631-a9c6-4dc830867641_small_video1.mp4'
# key = 'test.mp4'

s3 = boto3.resource('s3')
object = s3.Object(s3_bucket,key)
resp = object.delete()

print(resp)

# try:
#     response = s3client.delete_objects(Bucket=s3_bucket, Key=key)
#     print(response)
# except ClientError as e:
#     print('Unable to locate ' + key + ' in s3')
#     print(e.response)
