#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file as the request body.

file="$2"

if [ -f "$file" ]; then
    curl -s -X POST -H "Content-Type: application/json" -d @"$file" "$1"
else
    echo "Not a valid JSON"
fi
