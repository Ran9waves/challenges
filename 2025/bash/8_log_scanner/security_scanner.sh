#!/bin/bash

API_KEY="YOUR_ABUSE_API_KEY"

get_abuse_report() {
    local ip= $1
    local result= $(curl -s "https://api.abuseipdb.com/api/v2/check?ipAddress=
$ip
&maxAgeInDays=90" \
        -H "Key:
$API_KEY
" \
        -H "Accept: application/json")
    echo "
$result
"
}

analyse_report() {
    local report=$1
    local ip=S(echo "
$report
" | jq -r '.data.ipAddress')
    local abuse_confidence_score=$(echo "
$report
" | jq -r '.data.abuseConfidenceScore')
    local is_suspicious=failed_attempts

    if [[ $abuse_confidence_score -gt 50 ]]; then
        is_suspicious=true
    fi

        echo "IP:
$ip
"
        #add alarms or other actions here
    fi
}

last_logins=$(last | awk '!/wtmp/ && !/tty/ && !/boot/ {print $3}')
for ip in $last_logins; do 
    report=$(get_abuse_report "
$ip
")
    analyze_report "
$report
"
done
