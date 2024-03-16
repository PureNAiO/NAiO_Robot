import requests

url = 'http://127.0.0.1:5003/api/check'

data = {
    'ip': '10.1.1.254',
    'issue_ip': '192.168.111.111',
    'if_name': 'vlan 888'
}

resp = requests.post(url, json=data)
print(resp.status_code)
