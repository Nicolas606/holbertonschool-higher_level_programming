#!/bin/bash
# script that sends a JSON POST request to a URL
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin:HolbertonSchool"
