import json
import os
from pprint import pprint
from cisco_nexus_hyperfabric_rest_api_client import AuthenticatedClient
from cisco_nexus_hyperfabric_rest_api_client.models import models_fabric 
from cisco_nexus_hyperfabric_rest_api_client.types import Response
from cisco_nexus_hyperfabric_rest_api_client.api.fabrics import fabrics_get_all_fabrics

authToken = os.environ.get('AUTH_TOKEN')

def main():
    client = AuthenticatedClient(base_url="https://hyperfabric.cisco.com", token=authToken)
    response: Response[models_fabric] = fabrics_get_all_fabrics.sync_detailed(client=client)
    fabrics = json.loads(response.content)
    pprint(fabrics)

if __name__ == "__main__":
    main()
