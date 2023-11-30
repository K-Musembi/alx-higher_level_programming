#!/bin/bash
# Display size of body of response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
