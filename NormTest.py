#!/usr/bin/python3

import requests

resp = requests.get("http://api.open-notify.org/astros.json")

print(resp.json())
