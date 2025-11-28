#!/bin/bash

echo "Insert your command: "
read user_command

case $user_command in
    "ls")
        echo "command allowed"
        echo "Listing files..."
        ls
        ;;
    "pwd")
        echo "command allowed"
        echo "Current directory:"
        pwd
        ;;
    *)
        echo "you have no permissions to run this command"
        exit 1
        ;;
esac