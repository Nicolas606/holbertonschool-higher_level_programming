#!/bin/bash
# Only status code
curl -s -o /dev/null --head --write-out '%{http_code}' "$1"
