from ncclient import manager

m = manager.connect(
    host="ios-xe-mgmt.cisco.com",
    port=10000,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
    )

#test Rev03
#test Rev04
#test Rev05
#test Rev05_Branches

netconf_reply = m.get_config(source="running")
print(netconf_reply)

