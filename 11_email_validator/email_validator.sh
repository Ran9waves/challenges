#! /bin/bash

#this function validates email addresses using RegEx

validateEmail (){
    email=$1
    pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if [[ $email =~ $pattern ]]; then
        echo "Valid email address"
    else
        echo "Invalid email address"
    fi
}

# prompt user for email address
echo "Enter an email address to validate: "
read emailInput

#Call the function with the user input
validateEmail "$emailInput"
