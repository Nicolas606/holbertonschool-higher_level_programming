#!/usr/bin/python3
""" script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id  """
import requests
from sys import argv

if __name__ == "__main__":
    userName = argv[1]
    userpass = argv[2]
    url = 'https://api.github.com/user'

    req = requests.get( url, auth=('userName', 'userpass'))
    try:
        print(req.json().get('id'))
    except:
        print('None')
