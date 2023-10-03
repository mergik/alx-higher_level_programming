#!/usr/bin/python3
"""
Python script that takes GitHub credentials
to display id using GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, token))
    data = response.json()

    if 'id' in data:
        print(data['id'])
    else:
        print("Not Found")
