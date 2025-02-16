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
        return 1
    except requests.exceptions.RequestException as e:
        if e.response is not None and e.response.status_code == 409:
            logger.warning(f"VRF '{vrf_name}' already exists. Skipping")
            return 1
        logger.error(f"Failed to create VRF: {e}")
        return None

def create_vni(fabric_id, vni_name, vnid, vni_descr, vrf_name, members, svis):
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
          "members": members,
          "svis": svis,
          "vrfId": vrf_name
        }
       ]
      } 
    try:
        response = requests.post(url, headers=headers, json=payload, verify=True)
        response.raise_for_status()
        vni_data = response.json()
        logger.info(f"VNI '{vni_name}' created successfully.")
        return 1
    except requests.exceptions.RequestException as e:
        if e.response is not None and e.response.status_code == 409:
            logger.warning("VNI already exists. Skipping.")
            return 1
        error_message = e.response.json()
        logger.error(f"API error message: {error_message}") 
        return None

def main():
    fabric_id = "BRU-AUTOMATION"
    vrf_name  = "VRF-One"
    vni_configurations = [
          {
            "name": "network-one",
            "description": "logical network one",
            "vnid": 12000,
            "members": [
                {
                    "port": {"portName": "Ethernet1_5", "nodeName": "node-LEAF0"},
                    "vlanId": 100,
                    "untagged": False
                },
                {
                    "port": {"portName": "Ethernet1_5", "nodeName": "node-LEAF1"},
                    "vlanId": 100,
                    "untagged": False
                }
            ],
            "svis": [
                {
                    "enabled": True,
                    "ipv4Addresses": ["192.168.66.1/24"],
                    "ipv6Addresses": ["2001::1/64"],
                    "vlanId": 100
                }
            ]
          },
          {
            "name": "network-two",
            "description": "logical network two",
            "vnid": 12001,
            "members": [
                {
                    "port": {"portName": "Ethernet1_5", "nodeName": "node-LEAF0"},
                    "vlanId": 200,
                    "untagged": False
                },
                {
                    "port": {"portName": "Ethernet1_5", "nodeName": "node-LEAF1"},
                    "vlanId": 200,
                    "untagged": False
                }
            ],
            "svis": [
                {
                    "enabled": True,
                    "ipv4Addresses": ["192.168.67.1/24"],
                    "ipv6Addresses": ["2002::1/64"],
                    "vlanId": 200
                }
            ]
          }
        ]
   
    vrf_id = create_vrf(fabric_id, vrf_name)
    if not vrf_id:
        logger.error("Failed to create VRF. Exiting.")
        return

    for vni_config in vni_configurations:
        vni_result = create_vni(
            fabric_id,
            vni_config["name"],
            vni_config["vnid"],
            vni_config["description"],
            vrf_name, #Vrf name is accepted in vrfId, the API is forgiving!
            vni_config["members"],
            vni_config["svis"]
        )
        if not vni_result:
            logger.error("Failed to create VNI. Exiting.")
            break

    logger.info("VRF and VNI creation process completed successfully.")

if __name__ == "__main__":
    main()
