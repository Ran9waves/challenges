#!/bin/bash

check_never_expire_passwords() {
    echo "Users with never expire password: "
    echo "======================================="
    awk -F: '($2=="*" || $2=="!!") {print $1}' /etc/shadow
    echo ""
}