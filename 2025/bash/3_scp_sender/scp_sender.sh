#!/bin/bash

# This script sends a file to a remote server using SCP
remote_host="ip_address_or_hostname"
remote_user="username"
filename="path_to_file_to_transfer"

# Lists files in the remote directory before transferring the file and stablishes connection with remote_host
ssh $remote_user@$remote_host "ls -l" $filename >/dev/null 2>&1
#if the connection is stablished with host
if [ $? -eq 0 ]; then
    echo "Connected to $remote_host, preparing to transfer file..."
    # Transfers the file to the /tmp/backup directory on the local machine
    scp $remote_user@$remote_host:$filename /tmp/backup
        if [ $? -eq 0 ]; then
            echo "Connected to $remote_host, transferring file..."
            #removes filename after transfer
            rm -rf $filename
            echo "File transferred successfully and original file removed."
        else
            #in case the transfer fails, it shows the error code and exits with status 1
            echo "File transfer failed."
            echo "error code: $?"
            exit 1
else
    #in case the connection to $remote_host fails, show error code and exits with status 1
    echo "Failed to connect to $remote_host or list files."
    echo "error code: $?"
    exit 1
fi
