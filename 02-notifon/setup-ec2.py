# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
img = ec2.Image('ami-922914f7')
key = ec2.KeyPair('python_automation_key')
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst= instances[0]
inst.wait_until_running()
print(inst.public_dns_name)
