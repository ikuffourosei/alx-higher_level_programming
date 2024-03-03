#!/bin/bash
# a Bash script that sends a GET request to the URL and displays the body of the response with header variable:value
curl -sX GET -H "X-School-User-Id: 98" "$1"
