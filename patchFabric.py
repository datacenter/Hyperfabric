import requests
import os

token = os.environ['AUTH_TOKEN']
fabricId = '0bf78152-ced0-47ac-885a-f799687f8313'
url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabricId}"

#
# GET fabrics/{id} returns this
#
# {'fabricId': 'id', 
#  'name': 'N', 
#  'description': 'D', 
#  'location': 'L', 
#  'address': 'A', 
#  'city': 'C', 
#  'country': 'C', 
#  'labels': ['foo', 'bar'], 
#  'annotations': [
#        {'name': 'color', 
#         'value': 'blue', 
#         'dataType': 'STRING'}, 
#        {'name': 'isTest',
#         'value': 'true',
#         'dataType': 'BOOL'}
#        ]
# }
#

payloadList = ["{'description': 'REST API'}",
               '{"description": "REST API"}',
               "{description: 'REST API'}",
               "{description: \"REST API\"}"]

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

for payload in payloadList:
    print(f"sending payload {payload}")
    response = requests.request('PUT', url, headers=headers, data=payload)
    print(response.json())

