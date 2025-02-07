import requests
import os
import sys
import json

token = os.environ['AUTH_TOKEN']

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

def commitChanges(fabName: str) -> requests.Response:
    url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/candidates/default"
    payload = {"comments": "Automated commit"}
    response = requests.post(url, headers=headers, json=payload)
    return response

def main(fabName: str) -> requests.Response:
    payload = {
      "fabrics": [
        {
          "name": f"{fabName}",
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

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 409:
        sys.exit("Fabric already exists")
    fabrics = response.json()
    print(fabrics)
    commit = commitChanges(fabName)
    print("Committing changes ..")
    print(commit.json())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"Usage {sys.argv[0]} <fabricName>")
    url = "https://hyperfabric.cisco.com/api/v1/fabrics"
    fabName = sys.argv[1]
    main(fabName)

