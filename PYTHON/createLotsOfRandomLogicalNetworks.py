import requests
import json
import os
import logging
import random
from typing import Dict, List

##############################################
# This code generates 100 logical networks   #
# each with one IPv4 and IPv6 anycast gw     #
# and two VLAN bindings on two leaf switches #
# It assumes a fabric exists.                #
##############################################

AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
BASE_URL = "https://hyperfabric.cisco.com/api/v1"
FABRIC_ID = "BRU-AUTOMATION" 
VRF_NAME = "VRF-One"

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
        response = requests.post(url, headers=headers, json=payload, verify=True) #Disable SSL verification for lab
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
        response = requests.post(url, headers=headers, json=payload, verify=True) #Disable SSL verification for lab
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

def generate_random_ipv4():
    # Generate four random octets for IPv4
    return f"{random.randint(1, 223)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}/24"

def generate_random_ipv6():
    # Generate 8 random hex groups for IPv6, simplified for example
    return f"2001:db8:{random.randint(0, 0xffff):x}:{random.randint(0, 0xffff):x}:{random.randint(0, 0xffff):x}:{random.randint(0, 0xffff):x}:{random.randint(0, 0xffff):x}:{random.randint(0, 0xffff):x}/64"

def main():
    fabric_id = "BRU-AUTOMATION"
    vrf_name  = "VRF-One"
    num_vnis = 50
    base_vni = 12000

    vni_configurations = []
    for i in range(num_vnis):
        vlan_id  = random.randint(1, 4094)
        vni_name = f"network-{i + 1}"
        vni_descr = f"Logical network {i + 1}"
        vnid = base_vni + i  # Unique VNI ID

        vni_members = [
            {
                "port": {"portName": "Ethernet1_5", "nodeName": "node-LEAF0"},
                "vlanId": vlan_id,
                "untagged": False
            },
            {
                "port": {"portName": "Ethernet1_5", "nodeName": "node-LEAF1"},
                "vlanId": vlan_id,
                "untagged": False
            }
        ]
        svis = [
            {
                "enabled": True,
                "ipv4Addresses": [generate_random_ipv4()],
                "ipv6Addresses": [generate_random_ipv6()],
                "vlanId": vlan_id
            }
        ]

        vni_configurations.append({
            "name": vni_name,
            "description": vni_descr,
            "vnid": vnid,
            "members": vni_members,
            "svis": svis
        })

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
            logger.error(f"Failed to create VNI '{vni_config['name']}'. Continuing...")

    logger.info("VRF and VNIs creation process completed.")

if __name__ == "__main__":
    main()
