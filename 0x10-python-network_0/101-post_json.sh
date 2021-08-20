#!/bin/bash
# script that sends a JSON POST request to a URL
curl -s -X POST -H "Content-Type: applocation/json" -d @"$2" "$1"
