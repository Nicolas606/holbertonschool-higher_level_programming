#!/bin/bash
# Use a POST varible
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
