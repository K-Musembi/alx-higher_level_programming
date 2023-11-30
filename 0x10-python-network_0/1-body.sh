#!/bin/bash
# Display body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep 200 >/dev/null && curl -s "$1"
