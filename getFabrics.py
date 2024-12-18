import requests
import os
from pprint import pprint

url = "https://hyperfabric.cisco.com/api/v1/fabrics"
token = os.environ['AUTH_TOKEN']

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

payload = None
headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

response = requests.request('GET', url, headers=headers, data = payload)
pprint(response.json())


