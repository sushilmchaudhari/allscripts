import boto3

client = boto3.client('sqs')
sqs = boto3.resource('sqs')

#queuename = sqs.get_queue_by_name(QueueName='msri-vod-test')
queURL = "https://sqs.us-west-1.amazonaws.com/675436952689/msri-vod-test"

params = {'guid': { 'DataType': 'String', 'StringValue': '77c54c4f-3599-46a9-8475-7d09e8e11229'},
          'origVideoName': {'DataType': 'String', 'StringValue': 'toystory22.mp4'},
          'newVideoName': {'DataType': 'String', 'StringValue': '00_999999_toystory22.mp4'}
         }

messageBody = 'SQS test -> 1'

response = client.send_message(QueueUrl=queURL, MessageBody=messageBody, MessageAttributes=params)
print "MessageId - ", response['MessageId']

#for i in range(10,15):
#    params = {'guid': { 'DataType': 'String', 'StringValue': '123' + str(i) },
#              'vid_new_name': {'DataType': 'String', 'StringValue': 'hello_test_' + str(i) +'.mp4'},
#         }
#    messageBody = 'Test message -> ' + str(i)
#    print params
#    print messageBody
#    response = client.send_message(QueueUrl=queURL, MessageBody=messageBody, MessageAttributes=params, DelaySeconds=10)
#    print "MessageId - ", response['MessageId']

#print(response.get('MessageId'))

#for message in queuename.receive_messages(MessageAttributeNames=['All']):
    # Get the custom author message attribute if it was set
#    if message.message_attributes is not None:
#        video_name = message.message_attributes.get('newVideoName').get('StringValue')
#        workshop_id = message.message_attributes.get('guid').get('StringValue')
#    print(message.body)
#    message.delete()

#message.delete()

#response = client.delete_message(
#    QueueUrl=queURL,
#    ReceiptHandle='AQEBCau/4K0nzFe+qOdPWqO7LqV3emDHzq9uLHFOVmGs874HTVdFu4/qJ+oWM/TAu+d68xQBaZHAmxHpFVvViTVJSv7IceOjdO49Vj7pSAxdZ6v/IWAFHudZ4WCRvUqVWSYSxwT+6ZigXnPJef4FXEc4SweqExVZ/jFAtT1N14doQlkzwKgEXoMZUk3Yvc3f2v0BkthsdhQF8ELyfTWe/dZgYqbAtsR3/Kq+01OWXOOFU/7eB0OZubggPOQXw1GQGCUdVsneQfA5YuLtFE2eZjsAIdi0SQY32QAy0nPJN4iVKvcjxHiBEgLTiEwc6ZdK80ji8pzfkKc44OJp738Vks0tR/Xrx0Y55bNqfwSTQxh8NH92yIOOT3QnAWQcTjzglvt5lvGpUS0y7kBtCGJl11CcIA=='
#)
