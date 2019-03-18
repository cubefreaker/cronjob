import requests
from requests.auth import HTTPBasicAuth

data = {"Cluster":"1"}
url = 'https://antavaya.opsifin.com/opsifin_api_balance'

try:
	requests.post(url, data=data, auth=HTTPBasicAuth('opsifin','opsifin123'))
	print('200')
except:
    print('post error')