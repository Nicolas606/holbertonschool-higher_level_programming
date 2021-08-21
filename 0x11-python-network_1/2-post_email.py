#!/usr/bin/python3
""" POST an email #0"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode('utf-8')

    html = urllib.request.Request(url, data)

    with urllib.request.urlopen(html) as response:
        print(response.read().decode('utf-8'))
