# coding: utf-8

import json
import urllib.request

req = urllib.request.Request(
    "https://nh-a811fa16.herokuapp.com",
    method='GET'
)

response_dic = {}
with urllib.request.urlopen(req) as response:
    response_dic = json.loads( response.read().decode("utf-8") )


print(response_dic)
