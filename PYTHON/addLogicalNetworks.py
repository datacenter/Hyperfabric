import requests
import json
import os
import logging

AUTH_TOKEN = os.environ['AUTH_TOKEN']
BASE_URL = "https://hyperfabric.cisco.com/api/v1"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
}

def create_vrf(fabric_id, vrf_name):
    url = f"{BASE_URL}/fabrics/{fabric_id}/vrfs"
    payload = {
        "vrfs": [
            {
                "name": vrf_name,
                "enabled": True
            }
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, verify=True)
        response.raise_for_status()
        vrf_data = response.json()
        logger.info(f"VRF '{vrf_name}' created successfully.")
        return vrf_data['vrfs'][0]['id']
    except requests.exceptions.RequestException as e:
        if e.response is not None and e.response.status_code == 409:
            logger.warning(f"VRF '{vrf_name}' already exists. Skipping")
            return 1
        logger.error(f"Failed to create VRF: {e}")
        return None

def create_vni(fabric_id, vni_name, vnid, vni_descr, vrf_id, ipv4_gw):
    url = f"{BASE_URL}/fabrics/{fabric_id}/vnis"
    payload = {
      "vnis": [
        {
          "name": f"{vni_name}",
          "description": f"{vni_descr}",
          "labels": [
            "preproduction",
          ],
          "enabled": True,
          "vni": vnid,
          "members": [
            {
              "port": {
                "portName": "Ethernet1_5",
                "nodeName": "node-LEAF0"
              },
              "vlanId": 100,
              "untagged": False
            },
            {
              "port": {
                "portName": "Ethernet1_5",
                "nodeName": "node-LEAF1"
              },
              "vlanId": 100,
              "untagged": False
            }
          ],
          "svis": [
            {
              "enabled": True,
              "ipv4Addresses": [ipv4_gw],
              "vlanId": 100
            }
          ]
        }
       ]
      } 
    try:
        response = requests.post(url, headers=headers, json=payload, verify=True)
        response.raise_for_status()
        vni_data = response.json()
        logger.info(f"VNI '{vni_name}' created successfully.")
        return vni_data
    except requests.exceptions.RequestException as e:
        if e.response is not None and e.response.status_code == 409:
            logger.warning("VNI already exists. Skipping.")
            return 1
        logger.error(f"Failed to create VNI: {e}")
        return None

def main():
    fabric_id = "BRU-AUTOMATION"
    vrf_name  = "VRF-One"
    vni_name  = "network-one"
    ipv4_gw   = "192.168.1.1/24"
    vnid      = 12000
    vni_descr = "logical network one"

    vrf_id = create_vrf(fabric_id, vrf_name)
    if not vrf_id:
        logger.error("Failed to create VRF. Exiting.")
        return

    vni_result = create_vni(fabric_id, vni_name, vnid, vni_descr, vrf_id, ipv4_gw)
    if not vni_result:
        logger.error("Failed to create VNI. Exiting.")
        return

    logger.info("VRF and VNI creation process completed successfully.")

if __name__ == "__main__":
    main()
