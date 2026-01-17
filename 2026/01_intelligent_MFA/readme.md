# INTELLIGENT MFA

This project pretended to emulate what could be a good solution of secure login based on MFA that applied different layers of security depending on the role and behavior of the user. 

# How it works

## STEP 1

In the first step of this login system, the user will identify himself/herself with an EMAIL and the PASSWORD selected by him/her.

The email will be used to:
- The role of the user: ADMIN or REGULAR
- Check the IP of the user. (1 point)
- Check the TIME of login. (if not regular work hours, 1 point)
- Check the LOCATION of the user. (if not regular location, 1 point)

If a REGULAR user scores 2 points or more, STEP 3 will be required for user.

If an ADMIN user scores 2 points, a alert (ticket) is sent to SOC, for follow-up. (possible investigation). STEP 3 is always mandatory for ADMIN.

## STEP 2
If STEP 1 is performed successfully (correct user and password), user will receive a challenge (OTP).

If the code is received and introduced correctly by the REGULAR user, user can access to the system (or access to STEP 3 in case he scored at least 2 or more points in STEP 1).

If the code is received and introduced correctly by the ADMIN user, user can move to STEP 3. 

If the code introduced by the user is wrong:
- user can retry it 2 more times.

If user fails these 2 attemps, then:
- user will be blocked 15 minutes. 
- if user fails the next attempt, user will be blocked for 30 mins.
- if user fails again, user will be blocked 1 hour. 

After the 3rd fail, user will have to contact IT team for unblocking. 

## STEP 3 
User introduces personal yubikey with FIDO2 for last step of login, else, he/she can't finish the log in. 




