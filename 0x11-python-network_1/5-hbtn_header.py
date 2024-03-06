#!/usr/bin/python3
"""a Python script that displays the value of the X-Request-Id
Usage: ./5-hbtn_header <url>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
