#users dummy mock data

import pyotp

HQ_IPS = ["10.0.0.5", "10.0.0.6"]
HQ_LOCATION = "Palo Alto"

#dummy database
users = {
    "Regular Joe": {
        "password":"password123", #store hashed in real implementation
        "role":"regular",
        "allowed_ips": ["192.168.1.10", "203.0.114.5"],
        "allowed_locations": ["Palo Alto"],
        "users_working_hours":(9,17), # from 9:00 to 17:00
        "opt_secret": pyotp.random_base32(),
        "fido_keys":[],
        "failed_otp_attempts":0,
        "otp_block_until": None

    },
    "Admin Jack":{
        "password":"admin123", #store hashed in real implementation
        "role":"admin",
        "allowed_ips": ["10.0.0.5"],
        "allowed_locations": ["New York"],
        "working_hours":(9,18), # from 9:00 to 18:00
        "opt_secret": pyotp.random_base32(),
        "fido_keys":[],
        "failed_otp_attempts":0,
        "otp_block_until": None
    }
}