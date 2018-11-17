
import boto3

sns = boto3.client('sns')

resp = sns.publish(
      Message='Insufficient Arguments to SQS message :',
      Subject=' Insufficient Arguments ',
      TargetArn='arn:aws:sns:us-west-1:675436952689:msri-vod-test-NotificationSns-14Q9GAF8RLEQ1')

print resp
