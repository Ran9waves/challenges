#!/bin/bash

#sets the time limit to see if a file has changed
file_to_check="/path/to/your/file"
time_limit=60

#gets original modification time of the file
initial_time=$(stat -c %Y "$file_to_check")

#captures SIGINT and SIGTERM to exit gracefully
trap "echo 'Exiting file checker script. Cleaning operations are in progress'; exit 1" SIGINT SIGTERM

#gets the initial modification time of the file
while true; do
    current_time=$(stat -c %Y "$file_to_check")

    if [ "$current_time" != "$initial_time" ]; 
        then
            echo "The file $file_to_check has been modified."
            initial_time=$current_time
        else
            elapsed_time=$(( $date +$s) - $initial_time )
            if [ $elapsed_time -gt $time_limit ]; then
                echo "No changes detected in $file_to_check for $time_limit seconds. Exiting."
                exit 1
            fi
        fi
    sleep 1
done
