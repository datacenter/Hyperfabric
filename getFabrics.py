import requests
import os
from pprint import pprint

token = os.environ['AUTH_TOKEN']

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

def main():
    url = "https://hyperfabric.cisco.com/api/v1/fabrics"
    response = requests.request('GET', url, headers=headers)
    fabrics = response.json()
    for fabric in fabrics['fabrics']:
        pprint(fabric)
        print(80*"=")

if __name__ == "__main__":
    main()

