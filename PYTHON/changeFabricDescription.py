import requests
import json
import os
import random
import sys
import logging


token = os.environ['AUTH_TOKEN']

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

baseUrl = "https://hyperfabric.cisco.com/api/v1"

birdNames = [
    "Eagle", "Hawk", "Owl", "Falcon", "Vulture", 
    "Crow", "Raven", "Robin", "Bluejay", "Cardinal", 
    "Sparrow", "Pigeon", "Dove", "Swallow", "Hummingbird", 
    "Woodpecker", "Wren", "Tufted Titmouse", "Chickadee", "Nuthatch", 
    "Bluebird", "Oriole", "Goldfinch", "Canary", "Parrot", 
    "Macaw", "Peacock", "Swan", "Goose", "Duck", 
    "Flamingo", "Penguin", "Ostrich", "Emu", "Kiwi", 
    "Albatross", "Pelican", "Heron", "Egret", "Ibis", 
    "Kingfisher", "Woodcock", "Snipe", "Sandpiper", "Gull", 
    "Seagull", "Albatross", "Puffin", "Pelican", "Flamingo"
]

birdAdjectives = [
    "Agile", "Ancient", "Aquatic", "Arboreal", "Avian",
    "Beautiful", "Bold", "Colorful", "Curious", "Elegant",
    "Endemic", "Exotic", "Feathered", "Fierce", "Flying",
    "Graceful", "Gregarious", "Ground-dwelling", "Intelligent", "Large",
    "Luminous", "Majestic", "Migratory", "Nocturnal", "Oceanic",
    "Omnivorous", "Plumaged", "Powerful", "Quick", "Rare", "Resilient",
    "Scavenging", "Secretive", "Sedentary", "Soaring", "Solitary",
    "Swift", "Terrestrial", "Tiny", "Tropical", "Vibrant",
    "Wading", "Wandering", "Winged", "Wintering", "Yellow",
    "Young", "Zesty", "Zippy", "Zoomorphic"
]

headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Authorization": "Bearer " + token,
}

def generateBirdName() -> str:
    randomAdjective = random.choice(birdAdjectives)
    randomBird = random.choice(birdNames)
    return f"{randomAdjective} {randomBird}"

def commitChanges(fabName: str) -> None:
    url = f"{baseUrl}/fabrics/{fabName}/candidates/default"
    payload = {"comments": "Automated commit"}
    response = requests.request('POST', url, headers=headers, json=payload, verify=True)
    logger.info(response.json())

def main(fabName: str) -> requests.Response:
    # Get the current definition
    # the data model is {"fabricId": string, 
    #                    "name": string, 
    #                    "description": string, 
    #                    "location": string, 
    #                    "address": string}
    #
    url = f"{baseUrl}/fabrics/{fabName}"
    response = requests.request('GET', url, headers=headers, verify=True)
    if response.status_code != 200:
        sys.exit("Does this fabric exist?")
    fabric = response.json()
    logger.info(fabric)
    try: 
        curDescr = json.dumps(fabric['description'])
        logger.info(f"Current description ==> {curDescr}")
    except KeyError:
        logger.info("No current description set")
    # Update the description of the fabric and PUT the entire updated fabric structure
    fabric['description'] = generateBirdName()
    payload = json.dumps(fabric)
    response = requests.request('PUT', url, headers=headers, data=payload, verify=True)
    logger.info(f"Updated description ==> {json.dumps(fabric['description'])}")
    logger.info("Commit changes")
    commitChanges(fabName)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(f"Usage {sys.argv[0]} <fabricName>")
    fabName = sys.argv[1]
    main(fabName)
