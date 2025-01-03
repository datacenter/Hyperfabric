import requests
import json
import os
import random

token = os.environ['AUTH_TOKEN']
fabricId = '0bf78152-ced0-47ac-885a-f799687f8313'
url = f"https://hyperfabric.cisco.com/api/v1/fabrics/{fabricId}"

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

def generateBirdName():
    randomAdjective = random.choice(birdAdjectives)
    randomBird = random.choice(birdNames)
    return f"{randomAdjective} {randomBird}"

def main():
    # Get the current definition.
    response = requests.request('GET', url, headers=headers, verify=True)
    fabric = response.json()
    print(f"CURRENT DESCRIPTION ==> {json.dumps(fabric['description'])}")

    # Update the description of the fabric.
    fabric['description'] = generateBirdName()
    payload = json.dumps(fabric)
    response = requests.request('PUT', url, headers=headers, data=payload, verify=True)
    print(f"UPDATED DESCRIPTION ==> {json.dumps(fabric['description'])}")

if __name__ == "__main__":
    main()
