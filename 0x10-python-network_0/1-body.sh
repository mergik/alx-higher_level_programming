#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
