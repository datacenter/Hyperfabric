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

variable "nodes" {
  default = {
   1 = {
         name       = "fab1-leaf1",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDF000",
         description   = "Leaf 1",
         location      = "SJ01-1-101-AAA01",
         labels        = ["blue", "red", "green"]
       },
   2 = {
         name       = "fab1-leaf2",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDF001",
         description   = "Leaf 2",
         location      = "SJ01-1-101-AAA02",
         labels        = ["blue", "red", "green"]
       },
   3 = {
         name       = "fab1-leaf3",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDF002",
         description   = "Leaf 3",
         location      = "SJ01-1-101-AAA03",
         labels        = ["blue", "red", "green"]
       },
   4 = {
         name       = "fab1-leaf4",
         model_name = "HF6100-32D",
         roles      = ["LEAF"],
         serial_number = "ABCDF003",
         description   = "Leaf 4",
         location      = "SJ01-1-101-AAA04",
         labels        = ["blue", "red", "green"]
       },
   5 = {
         name       = "fab1-spine1",
         model_name = "HF6100-32D",
         roles      = ["SPINE"],
         serial_number = "ABCDF004",
         description   = "Spine 1",
         location      = "SJ01-1-101-AAA05",
         labels        = ["blue", "red", "green"]
       },
   6 = {
         name       = "fab1-spine2",
         model_name = "HF6100-32D",
         roles      = ["SPINE"],
         serial_number = "ABCDF005",
         description   = "Spine 2",
         location      = "SJ01-1-101-AAA06",
         labels        = ["blue", "red", "green"]
       }
 
  }
}

################################################
# Iterate through nodes obj and create nodes   #
################################################

resource "hyperfabric_node" "nodemap" {
  fabric_id  = hyperfabric_fabric.fab1.id
  for_each   = var.nodes
  name = each.value["name"]
  roles = each.value["roles"]
  serial_number = each.value["serial_number"]
  description = each.value["serial_number"]
  model_name = each.value["model_name"]
  location = each.value["location"]
  labels = each.value["labels"]
}

# this is how you can iterate through the nodemap
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
