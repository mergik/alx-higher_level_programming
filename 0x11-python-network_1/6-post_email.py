#!/usr/bin/python3
"""
Python script that takes in a URL and email address,
sends POST request to the URL with email as parameter,
and finally displays body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    response = requests.post(url, data=email)
    print(f"Your email is: {sys.argv[2]}")
