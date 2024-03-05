#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response."""


import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as page:
    resp = page.getheader('X-Request-Id')
    print(resp)
