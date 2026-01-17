#!/bin/bash

echo "Please, enter a number: "
read number

# Validates that the input is a numeric value
if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Invalid input. Please enter a valid number."
    exit 1
else
    while [ $number  -gt 0 ]; do
        echo "$number"
        ((number-1))
    done
    echo "Countdown finished!"
fi
