import random
import sys
import json
import os
import requests
import pprint

authToken = os.environ['AUTH_TOKEN']

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + authToken,
}

def deleteAllFabNodes(fabName,devRole):
    endpoint = f'https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/nodes'
    nodes = requests.request('GET', endpoint, headers=headers, verify=True)
    nodes = json.loads(nodes.text)
    if len(nodes) == 0:
        return 1
    for node in nodes['nodes']:
        if devRole in node['roles']:
            print(f"Deleting node {node['name']}")
            n = node['name']
            endpoint = f'https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/nodes/{n}'
            delete = requests.request('DELETE', endpoint, headers=headers, verify=True) 
            print(delete)

def genPayload(numDevices,devRole):
    nodeDict = {}
    nodes = []
    for i in range(numDevices):
        node = {
         "name": f"node-{devRole}{i}",
         "description": f"Example node {i}",
         "enabled": True,
         "serialNumber": f"SERIAL_{i}",
         "roles": [f"{devRole}"],
         "labels": [f"LABEL_{random.randint(1, 5)}"],
         "modelName": "HF6100-32D"
         }
        nodes.append(node)
    nodeDict['nodes']=nodes
    return nodeDict

def pushChanges(endpoint,payload):
    response = requests.request('POST', endpoint, headers=headers, json=payload, verify=True)
    fabric = response.json()
    print(f"Response ==> {json.dumps(fabric)}")

def main(fabName,numDevices,devRole):
    if numDevices == 0:
        status = deleteAllFabNodes(fabName,devRole)
        if status:
            sys.exit("Fabric has no devices")
    payload = genPayload(numDevices,devRole)
    url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/nodes"
    pushChanges(url,payload)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(f"Usage {sys.argv[0]} <fabName> <numDevices (0 deletes all 'devRole' nodes)> <devRole (leaf|spine)>")
    fabName = sys.argv[1]
    numDevices = int(sys.argv[2])
    devRole = sys.argv[3].upper()
    main(fabName,numDevices,devRole)

