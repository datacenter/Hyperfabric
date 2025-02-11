from   typing import Dict, List 
import random
import sys
import json
import os
import requests
import pprint
import logging

authToken = os.environ['AUTH_TOKEN']
baseUrl = 'https://hyperfabric.cisco.com/api/v1'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + authToken,
}


def deleteAllFabNodes(fabName: str, devRole: str) -> int:
    endpoint = f"{baseUrl}/fabrics/{fabName}/nodes"
    nodes = requests.request('GET', endpoint, headers=headers, verify=True)
    nodes = json.loads(nodes.text)
    if len(nodes) == 0:
        return 0
    for node in nodes['nodes']:
        if devRole in node['roles']:
            logger.info(f"Deleting node {node['name']}")
            n = node['name']
            endpoint = f'{baseUrl}/fabrics/{fabName}/nodes/{n}'
            delete = requests.request('DELETE', endpoint, headers=headers, verify=True) 
            logger.info(delete.status_code)
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

def pushChanges(endpoint: str, payload: Dict) -> int:
    logger.info(f"Pushing payload {payload} to URL {endpoint}")
    response = requests.request('POST', endpoint, headers=headers, json=payload, verify=True)
    fabric = response.json()
    logger.info(f"Response ==> {json.dumps(fabric)}")
    # HTTP 409 means a conflict exists
    return 0 if response.status_code == 409 else 1

def commitChanges(fabName: str) -> None:
    url = f"{baseUrl}/fabrics/{fabName}/candidates/default"
    payload = {"comments": "Automated commit"}
    logger.info("Committing changes ...")
    pushChanges(url,payload)

def fabricExists(fabName: str) -> int:
    url = f"{baseUrl}/fabrics/{fabName}"
    fabric = requests.request('GET', url, headers=headers, verify=True)
    return 1 if fabric.status_code == 200 else 0

def main(fabName: str, numDevices: int, devRole: str) -> None:
    if not fabricExists(fabName):
        sys.exit("No such fabric found!")
    if numDevices == 0:
        # user wants to delete all nodes with given role
        status = deleteAllFabNodes(fabName,devRole)
        if not status:
            sys.exit(f"Fabric has no {devRole} devices")
        # commit deletion and bail out
        sys.exit(commitChanges(fabName))
    # build the JSON payload for the number of devices required
    payload = genPayload(numDevices,devRole)
    url = f"{baseUrl}/fabrics/{fabName}/nodes"
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

