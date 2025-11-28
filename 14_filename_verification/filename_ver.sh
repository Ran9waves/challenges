#!/bin/bash

echo "insert filename: "
read filename
filename=$(echo $filename | tr -dc '[:alnum:]\n\r' | tr '[:upper:]' '[:lower:]')"
eval $filename