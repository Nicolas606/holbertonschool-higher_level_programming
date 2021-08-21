#!/usr/bin/python3
""" POST an email #1 """
import requests
from sys import argv

if __name__ == "__main__":
    html = requests.post(argv[1], {"email": argv[2]})
    print("{}".format(html.text))
