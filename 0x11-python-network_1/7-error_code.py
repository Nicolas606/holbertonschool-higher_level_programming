#!/usr/bin/python3
""" Error code #1 """
import requests
from sys import argv

if __name__ == "__main__":
    html = requests.get(argv[1])
    if(html.status_code < 400):
        print(html.text)
    else:
        print("Error code: {}".format(html.status_code))
