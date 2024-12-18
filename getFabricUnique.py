import requests
import os
from pprint import pprint

token = os.environ['AUTH_TOKEN']
fabricId = '0bf78152-ced0-47ac-885a-f799687f8313'
url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabricId}"

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

response = requests.request('GET', url, headers=headers)
print(response.json())


