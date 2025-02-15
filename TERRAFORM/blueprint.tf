variable "nodes" {
  default = {
   1 = {
         name       = "fab1-leaf1",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDL000",
         description   = "Leaf 1",
         location      = "SJ01-1-101-AAA01",
         labels        = ["blue", "red", "green"]
       },
   2 = {
         name       = "fab1-leaf2",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDL001",
         description   = "Leaf 2",
         location      = "SJ01-1-102-AAA02",
         labels        = ["blue", "red", "green"]
       },
   3 = {
         name       = "fab1-leaf3",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDL002",
         description   = "Leaf 3",
         location      = "SJ01-1-103-AAA03",
         labels        = ["blue", "red", "green"]
       },
   4 = {
         name       = "fab1-leaf4",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDL003",
         description   = "Leaf 4",
         location      = "SJ01-1-104-AAA04",
         labels        = ["blue", "red", "green"]
       },
   5 = {
         name       = "fab1-spine1",
         model_name = "HF6100-32D",
         roles      = ["SPINE"],
         serial_number = "ABCDS001",
         description   = "Spine 1",
         location      = "SJ01-1-105-AAA05",
         labels        = ["blue", "red", "green"]
       },
   6 = {
         name       = "fab1-spine2",
         model_name = "HF6100-32D",
         roles      = ["SPINE"],
         serial_number = "ABCDS002",
         description   = "Spine 2",
         location      = "SJ01-1-106-AAA06",
         labels        = ["blue", "red", "green"]
       }
 
  }
}

################################################
# Create fabric blueprint first - no nodes yet #
################################################

resource "hyperfabric_fabric" "fab1" {
  name        = "TF-FAB1"
  address     = "7b de kleetlaan"
  city        = "Diegem"
  country     = "BE"
  location    = "Peg3 TAC lab"
  description = "created by cpaggen using TF"
  labels = [
    "peg3",
    "lab",
    "CX",
    "Terraform"
  ]
  annotations = [
    {
      data_type = "STRING"
      name      = "owner"
      value     = "cpaggen"
    },
    {
      name  = "rack"
      value = "R251-B2"
    }
  ]
} 

################################################
# Iterate through nodes obj and create nodes   #
################################################

resource "hyperfabric_node" "nodemap" {
  fabric_id     = hyperfabric_fabric.fab1.id
  for_each      = var.nodes
  name          = each.value["name"]
  roles         = each.value["roles"]
  serial_number = each.value["serial_number"]
  description   = each.value["serial_number"]
  model_name    = each.value["model_name"]
  location      = each.value["location"]
  labels        = each.value["labels"]
}

output "all_node_names" {
    value = [for node in hyperfabric_node.nodemap : node.name]
}

################################################
# Configure fabric ports on all switches       #
################################################

resource "hyperfabric_node_port" "node1_eth1_1" {
  node_id = hyperfabric_node.nodemap.1.id
  name    = "Ethernet1_1"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node2_eth1_1" {
  node_id = hyperfabric_node.nodemap.2.id
  name    = "Ethernet1_1"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node3_eth1_1" {
  node_id = hyperfabric_node.nodemap.3.id
  name    = "Ethernet1_1"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node4_eth1_1" {
  node_id = hyperfabric_node.nodemap.4.id
  name    = "Ethernet1_1"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node1_eth1_2" {
  node_id = hyperfabric_node.nodemap.1.id
  name    = "Ethernet1_2"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node2_eth1_2" {
  node_id = hyperfabric_node.nodemap.2.id
  name    = "Ethernet1_2"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node3_eth1_2" {
  node_id = hyperfabric_node.nodemap.3.id
  name    = "Ethernet1_2"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node4_eth1_2" {
  node_id = hyperfabric_node.nodemap.4.id
  name    = "Ethernet1_2"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node5_eth1_1" {
  node_id = hyperfabric_node.nodemap.5.id
  name    = "Ethernet1_1"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node5_eth1_2" {
  node_id = hyperfabric_node.nodemap.5.id
  name    = "Ethernet1_2"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node5_eth1_3" {
  node_id = hyperfabric_node.nodemap.5.id
  name    = "Ethernet1_3"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node5_eth1_4" {
  node_id = hyperfabric_node.nodemap.5.id
  name    = "Ethernet1_4"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node6_eth1_1" {
  node_id = hyperfabric_node.nodemap.6.id
  name    = "Ethernet1_1"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node6_eth1_2" {
  node_id = hyperfabric_node.nodemap.6.id
  name    = "Ethernet1_2"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node6_eth1_3" {
  node_id = hyperfabric_node.nodemap.6.id
  name    = "Ethernet1_3"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node6_eth1_4" {
  node_id = hyperfabric_node.nodemap.6.id
  name    = "Ethernet1_4"
  roles   = ["FABRIC_PORT"]
  enabled = "true"
}

################################################
# Connect the nodes together as a Clos fabric  #
################################################

resource "hyperfabric_connection" "node1-spine1" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.1.node_id
    port_name = "Ethernet1_1"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.5.node_id
    port_name = "Ethernet1_1"
  }
}

resource "hyperfabric_connection" "node1-spine2" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.1.node_id
    port_name = "Ethernet1_2"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.6.node_id
    port_name = "Ethernet1_1"
  }
}

resource "hyperfabric_connection" "node2-spine1" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.2.node_id
    port_name = "Ethernet1_1"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.5.node_id
    port_name = "Ethernet1_2"
  }
}

resource "hyperfabric_connection" "node2-spine2" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.2.node_id
    port_name = "Ethernet1_2"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.6.node_id
    port_name = "Ethernet1_2"
  }
}

resource "hyperfabric_connection" "node3-spine1" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.3.node_id
    port_name = "Ethernet1_1"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.5.node_id
    port_name = "Ethernet1_3"
  }
}

resource "hyperfabric_connection" "node3-spine2" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.3.node_id
    port_name = "Ethernet1_2"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.6.node_id
    port_name = "Ethernet1_3"
  }
}

resource "hyperfabric_connection" "node4-spine1" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.4.node_id
    port_name = "Ethernet1_1"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.5.node_id
    port_name = "Ethernet1_4"
  }
}

resource "hyperfabric_connection" "node4-spine2" {
  fabric_id = hyperfabric_fabric.fab1.id
  local = {
    node_id   = hyperfabric_node.nodemap.4.node_id
    port_name = "Ethernet1_2"
  }
  remote = {
    node_id   = hyperfabric_node.nodemap.6.node_id
    port_name = "Ethernet1_4"
  }
}

################################################
# Make eth1/5 a host port on node-1 and node-2 #
################################################

resource "hyperfabric_node_port" "node1_eth1_5" {
  node_id = hyperfabric_node.nodemap.1.id
  name    = "Ethernet1_5"
  roles   = ["HOST_PORT"]
  enabled = "true"
}

resource "hyperfabric_node_port" "node2_eth1_5" {
  node_id = hyperfabric_node.nodemap.2.id
  name    = "Ethernet1_5"
  roles   = ["HOST_PORT"]
  enabled = "true"
}

################################################
# Create VRF and logical networks + anycast gw #
################################################

resource "hyperfabric_vrf" "vrf-one" {
  fabric_id = hyperfabric_fabric.fab1.id
  name      = "VRF-One"
}

resource "hyperfabric_vni" "network-one" {
  fabric_id   = hyperfabric_fabric.fab1.id
  name        = "network-one"
  description = "Network one VNI"
  vni         = 10000
  svi = {
    enabled        = true
    ipv4_addresses = ["192.168.1.254/24"]
    ipv6_addresses = ["2001::1/64"]
  }                                     
  members = [
  {
      node_id   = hyperfabric_node.nodemap.1.node_id
      port_name = "Ethernet1_5" 
      vlan_id   = 100
    },
    {
      node_id   = hyperfabric_node.nodemap.2.node_id
      port_name = "Ethernet1_5"
      vlan_id   = 100
    } 
  ]
  vrf_id = hyperfabric_vrf.vrf-one.vrf_id
}      

resource "hyperfabric_vni" "network-two" {
  fabric_id   = hyperfabric_fabric.fab1.id
  name        = "network-two"
  description = "Network two VNI"
  vni         = 20000
  svi = {
    enabled        = true
    ipv4_addresses = ["192.168.2.254/24"]
    ipv6_addresses = ["2002::1/64"]
  }
  members = [ 
  {
      node_id   = hyperfabric_node.nodemap.1.node_id
      port_name = "Ethernet1_5"
      vlan_id   = 200
    },
    {
      node_id   = hyperfabric_node.nodemap.2.node_id
      port_name = "Ethernet1_5"
      vlan_id   = 200
    }
  ]
  vrf_id = hyperfabric_vrf.vrf-one.vrf_id
}
