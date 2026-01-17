#!/bin/bash

LOGFILE="/var/log/auth.log"
PATTERN="Failed password for invalid user"
RECIPIENT="email@youwant.com"
SUBJECT="Alert: failed login attempt detected"
BLOCK_THRESHOLD=3

declare -A failed_attempts

while IFS = read -r line; do
    if [[ $line =~$PATTERN ]]; then
    rhost=$(echo "
$line
" | awk -F'[= ]' '{print $(NF-4)}')
        user=$(echo"
$line
" | awk -F'[= ]' '{print $(NF-5)}')
        message+="rhost:
$rhost
, user:
$user
"$'\n'
        if [[ -n ${failed_attempts[$rhost]} ]]; then
            ((failed_attempts[$rhost]++))
        else    
            failed_attempts[$rhost]=1
        fi
        if (( failed_attempts[rhost] > BLOCK_THRESHOLD )); then
            ufw insert 1 deny from $rhost to any
        fi
    fi
done < "
$LOGFILE
"

if [[ -n $message]]; then
    echo -e "Invalid User Login Attempts detected \n
$message
" | mail -s "
$SUBJECT
" $RECIPIENT
fi

#to make this file executable, run the command below:
#chmod +x /path/to/log_scanner.sh

#to set up a cron job to run this script at a specific time interval, run crontab -e and add the command below: 
#1 0 * * * /path/to/log_scanner.sh