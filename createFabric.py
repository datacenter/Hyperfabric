import requests
import os

url = "https://hyperfabric.cisco.com/api/v1/fabrics"
token = os.environ['AUTH_TOKEN']
# token = '{token}'


payload = {
  "fabrics": [
    {
      "name": "CP-AUTOMATION-TEST",
      "description": "My DC Fabric",
      "address": "170 West Tasman Dr.",
      "city": "San Jose",
      "country": "United States of America",
      "location": "SJ1-1-AA1",
      "labels": ["prod", "blue"],
      "annotations": [
        {
          "name": "color",
          "value": "blue"
        },
        {
          "dataType": "BOOL",
          "name": "isDMZ",
          "value": "false"
        },
      ],
    },
  ]
}

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

response = requests.post(url, headers=headers, json=payload)
fabrics = response.json()
print(fabrics)

