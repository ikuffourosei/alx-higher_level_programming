#!/bin/bash
# a Bash script that takes in a URL and displays the size of the body of the response
curl -sI $1 | grep -i content-Length | awk '{print $2}'
