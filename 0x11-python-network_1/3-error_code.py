#!/usr/bin/python3
import urllib.request
import urllib.error
import sys


def display_response_content_or_error_code(url):
    """
    Sends a request to the given URL and displays the body of the response or
    the HTTP error code if an error occurs.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
        print(content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    display_response_content_or_error_code(url)
