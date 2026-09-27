#!/usr/bin/python3
"""Fetches the status of the ALU Intranet."""
import urllib.request

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    body = response.read()

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode("utf-8"))
