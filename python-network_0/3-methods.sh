#!/bin/bash
# Displays all HTTP methods accepted by a server
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d' ' -f2-
