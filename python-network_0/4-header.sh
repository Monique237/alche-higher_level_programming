#!/bin/bash
# Sends a GET request with the X-HolbertonSchool-User-Id header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
