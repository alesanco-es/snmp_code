from pysnmp.hlapi import *

def get_snmp_oid(ip, community, port, oid):
    # Create an SNMP GET request for the given OID
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((ip, port)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    # Process the response
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(f"Error: {errorIndication}")
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()} at {errorIndex}")
    else:
        for varBind in varBinds:
            print(f"{varBind[0]} = {varBind[1]}")

# Parameters
ip_address = '192.168.153.1'
community_string = 'public'
port = 163
oid = '1.3.6'

# Call the function
get_snmp_oid(ip_address, community_string, port, oid)
