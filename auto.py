import datetime
from netmiko import ConnectHandler

def ping(ip, issue_ip, if_name):
    device = {
        "device_type": "cisco_ios",
        "ip" : ip, 
        "port" : 22, 
        "username" : 'netadmin',
        "password" : 'P@ssw0rd4f1',
    }
    connect = ConnectHandler(**device)
    if_info = connect.send_command("show ip interface brief")
    ping_info = connect.send_command(f"ping {issue_ip}", read_timeout=30)
    report(if_name, if_info, ping_info)


def report(if_name, if_info, ping_info):
    temp = f'''
# Incident Report
UP|DOWN Incident found in CoreSW at GZ office
## {if_name}
* The command "show ip interface brief" result as
---
{if_info}
---
* The ping command to this interface as
---
{ping_info}
---

#### Please take above as reference to solve this issue

{str(datetime.datetime.now()).split('.')[0]}
'''
    with open('issue_report.md', 'w') as f:
        f.write(temp)