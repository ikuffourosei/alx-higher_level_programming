#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as page:
    body = page.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")
