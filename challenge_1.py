# https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products/1.json

# goal: get the product's name

import json

import requests # because it is a third party package, need to install it using pip from command line

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/products/1.json"
response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(type(response.status_code))
# print(response.text)
# print(type(response.text))

parsed_response = json.loads(response.text)

# print(type(parsed_response))
# print(parsed_response)

print("THE NAME IS:", parsed_response["name"])