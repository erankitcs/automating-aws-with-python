# coding: utf-8
import requests
url = ''  #Replace with Slack Webhook URL.
data = {"text" : "Hello Ankit !!!"}
requests.post(url,json=data)
