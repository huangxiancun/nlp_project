# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2019/12/17 3:31 PM

# File_name: 'test_demo.py'

"""
Describe: this is a demo!
"""

import requests
import json
import time

url = 'http://localhost:5005/consult'
s = time.time()
input = {}

print(type(input))
headers = {
 'Content-Type': 'application/json'
}
data = json.dumps(input)
print(type(data))

res = requests.post(url, data)
print(res)
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
print(time.time() - s)