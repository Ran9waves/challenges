#Helpers : risk scoring, IP/location simulation

from random import choice
from datetime import datetime
from users_data import HQ_IPS, HQ_LOCATION

def simulate_ip_and_location(username, user):
    """ This function simulates automatic detection of IP and location 
    for demo purposes.
    Users outside HQ may use VPN to appear in HQ."""

    remote_user = choice([True,False])

    if remote_user:
        vpn_used = choice([True, True, True, False]) #75% chance
        if vpn_used:
            ip = choice(HQ_IPS)
            location = HQ_LOCATION
            print("[INFO] remote user using VPN. Appears as HQ location.")
        else:
            ip = choice(["198.51.100.23","203.0.113.99"])
            location = choice(["New York", "Barcelona", "Paris"])
            print("[INFO] Remote user without VPN. Detected outside HQ.")
    else:
        ip = choice(HQ_IPS)
        location = HQ_LOCATION

    return ip, location

def calculate_risk(user, ip, location, login_hour): 
    score = 0
    if ip not in user["allowed_ips"]:
        score +=1
    if location not in user["allowed_locations"]:
        score +=1
    start_hour, end_hour = user['working_hours']
    if login_hour < start_hour or login_hour >= end_hour:
        score +=1
    return score