# Automating AWS with Python
Repository for the A Cloud Guru course *Automating AWS with Python*

## 03-videolyzer
Videolyzer is a project to perform video label detection on uploaded video in S3 and save response into DynamoDB using
Lambda Serverless.
Videolyzer currently has the following features:
- Upload Video to S3 bucket.
- Trigger event from S3 to Lambda Function to start Video Processing.
- Use SNS to identify completion of Label Detection Job and save into DynamoDB.

 
