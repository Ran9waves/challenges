#Intelligent MFA steps (1,2,3)

from users_data import users
from utils import simulate_ip_and_location, calculate_risk
from soc_alerts import send_soc_alert
import pyotp
from datetime import datetime, timedelta

def step1_login():
    print("=== Step 1: Login ===")
    username = input("Username: ")
    password = input("Password: ")

    if username not in users or users[username]['password'] != password:
        print("Invalid username or password.")
        return None, None
    
    user = users[username]
    ip, location = simulate_ip_and_location(username, user)
    print(f"[Info] Detected IP: {ip}, Location: {location}")

    risk_score = calculate_risk(user, ip, location)


#SOC alerts
    if user['role'] == 'admin' and risk_score >=2:
        send_soc_alert(username, "Suspicious activity in admin login")
    
    if user['role'] == 'regular' and risk_score >=2:
        send_soc_alert(username, "Suspicious activity in regular user login. Step 3 login requested.")
    
    return username, risk_score

# STEP 2: OTP Verification

def step2_otp(username):
    user = users[username]
    totp = pyotp.TOTP(user['otp_secret'])

    while user['failed_otp_attempts'] < 5:
        if user['otp_block_until']:
            if datetime.now() < user['otp_block_until']:
                wait_time = (user['otp_block_until'] - datetime.now()).seconds
                print(f"Account blocked for {wait_time} seconds.") #due failed OTP code
                return False
            else:
                user['otp_block_until'] = None
                user['failed_otp_attempts'] = 0
        
        code = input("Enter OTP code: ")
        if totp.verify(code):
            print("OTP verified successfully.")
            user['failed_otp_attempts'] = 0
            return True
        else:
            user["failed_otp_attempts"] += 1
            print(f"Incorrect OTP, Attempt {user['failed_otp_attempts']/5}")

            # Progressive blocking
            if user["failed_otp_attempts"] == 1:
                user['otp_block_until'] = datetime.now() + timedelta(minutes=5)
            elif user["failed_otp_attempts"] == 2:
                user['otp_block_until'] = datetime.now() + timedelta(minutes=15)
            elif user["failed_otp_attempts"] == 3:
                user['otp_block_until'] = datetime.now() + timedelta(minutes=30)
            elif user["failed_otp_attempts"] == 4:
                user['otp_block_until'] = datetime.now() + timedelta(hours=1)
            elif user["failed_otp_attempts"] == 5:
                print("Your account has been blocked. Contact IT team for support.")
                return False
    return False

# Step 3: Yubikey / FIDO2 Verification
# 
def step3_yubikey(username):
    print("=== Step 3: Yubikey / FIDO2 ===")
    print("Simulating FIDO2 verification (in real implementation, integrate with WebAuthn)")
    print("Please, insert your yubikey, touch it and press Enter...")
    #Here you would verify against stored FIDO2 credentials
    print("Yubikey verified successfully!")
    return True