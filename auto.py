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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Incident Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
        }}
        h1, h2, h3 {{
            margin-top: 0;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 3px;
        }}
    </style>
</head>
<body>
    <h1>Incident Report</h1>
    <p>UP|DOWN Incident found in CoreSW at GZ office</p>
    <h2>{if_name}</h2>
    <p>The command "show ip interface brief" result as:</p>
    <pre><code>{if_info}</code></pre>
    <p>The ping command to this interface as:</p>
    <pre><code>{ping_info}</code></pre>
    <h4>Please take above as reference to solve this issue</h4>
    <p>{str(datetime.datetime.now()).split('.')[0]}</p>
</body>
</html>

'''
    with open('issue_report.md', 'w') as f:
        f.write(temp)