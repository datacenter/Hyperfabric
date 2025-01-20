# Cisco Nexus Hyperfabric Automation

This repository provides code samples to automate various tasks related to Cisco Nexus Hyperfabric. 

**What is Cisco Nexus Hyperfabric?**

[Cisco Nexus Hyperfabric](https://www.cisco.com/c/en/us/products/collateral/data-center-networking/nexus-hyperfabric/nexus-hyperfabric-ds.html) is a cloud-managed network fabric data-center solution, delivered as a service, that enables customers to easily design, deploy, manage, and scale multiple fabrics globally with a minimum of expertise.

**What's in this repository?**

This repository includes code samples written in Python to automate common Nexus Hyperfabric tasks such as:

* Fabric provisioning
* Fabric modifications
* ...

**Authentication**

All access to Cisco Nexus Hyperfabric requires a bearer token. Obtain a token by selecting 'API bearer tokens' after clicking on your username in the top right-hand corner of the screen once logged into [hyperfabric.cisco.com](https://hyperfabric.cisco.com)

Add the token as an environment variable by using ``` export AUTH_TOKEN=`cat AUTH_TOKEN` ``` for example, assuming you have saved the token in a local file called AUTH_TOKEN.
