import json

nodes = dict([("machine%d" % i, "192.168.77.%d" % (i+1)) for i in range (2,7)])

topo_nodes = []
for m, ip in nodes.items():
    topo_nodes.append({
        "node": {
            "hostnames": {"manage":[m], "storage":[ip]},
            "zone": 1
        },
        "devices": ["/dev/sdc", "/dev/sdd", "/dev/sde"]
    })gluster-kubernetes-1.2.0

topo = {
    "clusters": [{"nodes": topo_nodes }]
}

with open("topology.json", "w") as o:
    json.dump(topo, o, indent=2)
