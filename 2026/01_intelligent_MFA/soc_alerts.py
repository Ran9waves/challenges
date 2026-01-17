#Mocks SOC email sending

def send_soc_alert(username,reason):
    """
    Mocks sending an alert to SOC in case Step 2 detects an anomaly from user side due to score.
    In a real system, it could be replaced with smtplib or API integration"""

    print(f"[SOC ALERT] User: {username}, Reason: {reason}")
    return True