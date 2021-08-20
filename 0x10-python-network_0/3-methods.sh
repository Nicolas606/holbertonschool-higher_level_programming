#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.

curl -sI 0.0.0.0:5000/route_4 | awk '/Allow/ {print $2, $3, $4}'
