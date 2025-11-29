#!/bin/bash

echo "insert filename: "
read filename
filename=$(echo $filename | tr -dc '[:alnum:]\n\r' | tr '[:upper:]' '[:lower:]')"
eval $filename

#checks if the filename is trying to change the root directory
if [[ "$filename" == *..*; then
    echo "invalid input."
    exit 1
fi

#checks is the filename starts with "/"
if [[ "$filename" == /* ]]; then
    echo "invalid input."
    exit 1
fi

#checks if the filename is under certain directory
base_directory="/var/whateverdirectory"
full_path="$base_directory/$filename"
if [[ "$full_path" != "$base_directory/"* ]]; then
    echo "the file must be under $base_directory."
    exit 1
fi

#if all the checks are passed, print the file to the screen
cat "$full_path"
