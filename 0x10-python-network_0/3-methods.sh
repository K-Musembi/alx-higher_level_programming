#!/bin/bash
# Display accepted HTTP methods
curl -s -X OPTIONS -I "$1" | grep Allow
