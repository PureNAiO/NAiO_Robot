import requests

url = 'http://127.0.0.1:5003/api/check'

data = {'ip': '1.1.1.1',
        'en_pass': 'tea',
        'if_name': 'G1'}

resp = requests.post(url, json=data)
print(resp.json())