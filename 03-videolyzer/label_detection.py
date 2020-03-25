# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource("s3")
s3.create_bucket(Bucket="ankitvideolyzervideos",CreateBucketConfiguration={"LocationConstraints":session.region_name})
s3.create_bucket(Bucket="ankitvideolyzervideos",CreateBucketConfiguration={"LocationConstraint":session.region_name})
from pathlib import Path
bucket= s3.Bucket(name='ankitvideolyzervideos')
pathname = "D:\Tech\Automate AWS with Python\code\\automating-aws-with-python\\03-videolyzer\MyTestVideo.mp4"
path = Path(pathname).expanduser().resolve()
path.name
bucket.upload_file(str(path),str(path.name))
rekognition_client= session.client('rekognition')
response= rekognition_client.start_label_detection(Video={'S3Object':{'Bucket': bucket.name, 'Name': path.name}})
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result.keys()
result.keys()
result[JobStatus]
result[JobStatus]
result['JobStatus']
result['Lables']
result['Lables']
result['Labels']
result['Labels']['Name']
