from pysnmp.hlapi import *

# SNMP parameters
target_ip = '192.168.153.1'
community = 'public'
port = 163
oid = '1.3.6'

# Create an SNMP GET request
error_indication, error_status, error_index, var_binds = next(
    getCmd(SnmpEngine(),
           CommunityData(community),
           UdpTransportTarget((target_ip, port)),
           ContextData(),
           ObjectType(ObjectIdentity(oid)))
)

# Check for errors and process the response
if error_indication:
    print(f"Error: {error_indication}")
elif error_status:
    print(f"Error: {error_status.prettyPrint()} at {error_index and var_binds[int(error_index) - 1][0] or '?'}")
else:
    for var_bind in var_binds:
        print(f'{var_bind[0]} = {var_bind[1]}')
