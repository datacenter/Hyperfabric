from typing import Dict, List, Union

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

def deleteAllFabNodes(fabName: str, devRole: str) -> int:
    endpoint = f'https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/nodes'
    nodes = requests.request('GET', endpoint, headers=headers, verify=True)
    nodes = json.loads(nodes.text)
    if len(nodes) == 0:
        return 0
    for node in nodes['nodes']:
        if devRole in node['roles']:
            print(f"Deleting node {node['name']}")
            n = node['name']
            endpoint = f'https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/nodes/{n}'
            delete = requests.request('DELETE', endpoint, headers=headers, verify=True) 
            print(delete.status_code)
    return 1

def genPayload(numDevices: int, devRole: str) -> Dict[str, List[Dict]]:
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

def pushChanges(endpoint: str, payload: Dict) -> Union[Dict, int]:
    response = requests.request('POST', endpoint, headers=headers, json=payload, verify=True)
    fabric = response.json()
    print(f"Response ==> {json.dumps(fabric)}")
    if response.status_code == 409:
        # conflict, node(s) already present
        return 0
    else:
        return 1

def commitChanges(fabName: str) -> None:
    url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/candidates/default"
    payload = {"comments": "Automated commit"}
    print("Committing changes ...")
    pushChanges(url,payload)

def main(fabName: str, numDevices: int, devRole: str) -> None:
    if numDevices == 0:
        # user wants to delete all nodes with given role
        status = deleteAllFabNodes(fabName,devRole)
        if not status:
            sys.exit(f"Fabric has no {devRole} devices")
        # commit deletion and bail out
        sys.exit(commitChanges(fabName))
    # build the JSON payload for the number of devices required
    payload = genPayload(numDevices,devRole)
    url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabName}/nodes"
    if (pushChanges(url,payload)):
        # commit changes to the fabric if JSON payload was accepted by REST API
        commitChanges(fabName)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(f"Usage {sys.argv[0]} <fabName> <numDevices (0 deletes all 'devRole' nodes)> <devRole (leaf|spine)>")
    fabName = sys.argv[1]
    numDevices = int(sys.argv[2])
    devRole = sys.argv[3].upper()
    main(fabName,numDevices,devRole)

