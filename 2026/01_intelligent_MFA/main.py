#Main sequential flow

from mfa_steps import step1_login, step2_otp, step3_yubikey

def main():
    username, risk_score = step1_login
    if not username:
        print("Cannot proceed to Step 2 without successful login.")
        return
    
    if not step2_otp(username):
        print("Cannot proceed to step 3 without successful OTP verification.")
        return
    
    if not step3_yubikey(username):
        print("Login failed at Step 3. Please try again.")
        return
    
    print(f"User '{username}' logged in successfully with all MFA steps completed.")

if __name__ == "__main__":
    main()          

            

