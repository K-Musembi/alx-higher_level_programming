#!/bin/bash
# Display accepted HTTP methods
curl -s -X OPTIONS -i "$1"
