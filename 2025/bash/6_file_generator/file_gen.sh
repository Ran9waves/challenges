#!/bin/bash

file="/tmp/testfile"
if ! touch file 2>/dev/null; then
    echo "Error: Cannot create or write to $file. Check permissions."
    exit 1
else
    echo "File created successfully: $file"
fi