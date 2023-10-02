#!/bin/bash
# This script takes a URL as an argument, sends a POST request with specified parameters, and displays the body of the response.
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
