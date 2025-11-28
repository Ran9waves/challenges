import socket
import time
import requests

targets = [
    ("letsdefend.io", 80, "TCP"),
    ("letsdefend.io", 443, "TCP"),
    ("8.8.8.8", 80, "TCP") ]

SLACK_WEBHOOK_URL = "YOUR_SLACK_WEBHOOK_URL_HERE"

def check_port(target, port, protocol):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)

        if protocol == "TCP":
            result = s.connect_ex((target, port))
            s.close()
            return result == 0
    except Exception as e:
        print(f"Error checking port {port} on {target}: {e}")
        return False
        
def send_slack_notification(target, port, protocol):
    payload = { "text": f" {target}:{port}/{protocol} port not responding!"}
    print(payload)
    requests.post(SLACK_WEBHOOK_URL, json=payload)

while True:
    for target, port, protocol in targets:
        if not check_port(target, port, protocol):
            send_slack_notification(target, port, protocol)
    time.sleep(3600)
