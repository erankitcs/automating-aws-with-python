import urllib
import boto3

def start_label_detection(bucket, key):
    rekognition_client = boto3.client('rekognition')
    print('Starting Label Detection for bucket: {} and Video Name: {}'.format(bucket,key))
    response = rekognition_client.start_label_detection(
        Video={
            'S3Object':{
                'Bucket' : bucket,
                'Name' : key
            }
        }
    )
    print(response)
    return

def start_processing_video(event, context):
    print("Event Recieved..")
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        start_label_detection(
            bucket,
            urllib.parse.unquote_plus(key)
        )

    return
