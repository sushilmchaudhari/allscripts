import boto3
import httplib2
import errno
import socket
import json

def lambda_handler(event, context):
    client = boto3.client('lambda')
    websiteurl='' #enter your site url
    metriname='' #enter metric name 
    socketurl=websiteurl.split("/")[2]
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socketurl, 80))
    except socket.error, e:
        if 'Connection refused' in e:
            response=client.invoke(
                FunctionName='SendMetric', #paste real name of the lambda function you defined.
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 100,"MNAM": metriname}) 
            )
    else:
	h = httplib2.Http()
        h.force_exception_to_status_code = True
	resp, content = h.request(websiteurl, "GET")
        STAT=resp.status
        if STAT == 200 or STAT == 304:
            response=client.invoke(
                FunctionName='SendMetric', #paste real name of the lambda function.
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 200,"MNAM": metriname}) 
            )
        else:
            response=client.invoke(
                FunctionName='SendMetric',
                InvocationType='Event',
                LogType='Tail',
                Payload=json.dumps({"VAL": 50,"MNAM": metriname}) 
            )
