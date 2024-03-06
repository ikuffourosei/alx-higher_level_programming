#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
  - Handles HTTP errors.
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as resp:
            print(resp.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
