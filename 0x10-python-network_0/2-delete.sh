#!/bin/bash
# Send DELETE request and display response
curl -X DELETE -s -o /dev/null -w "%{http_code}" "$1" | grep 200 >/dev/null && curl -X DELETE -s "$1"
