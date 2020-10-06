# to fetch the interface details of a devices
from infoblox_netmri.client import InfobloxNetMRI
from pprint import pprint
import time

defaults = {
    "host": "10.*.*.*",
    "username": "admin",
    "password": "***********",
}

infoblox_client = InfobloxNetMRI(
    defaults.get("host"), defaults.get("username"), defaults.get("password"),
    api_version="3.*.*",
)
x = 'aj-test-switch'
querystring = {
        'op_DeviceName': "=",
        'val_c_DeviceName': x,
        'methods': "interfaces",
        'select': "interfaces",
}
devicedetails = infoblox_client.api_request('devices/find',querystring) # the interface details will be stored in devicedetails in multi-level dictionary
pprint(devicedetails['devices'])


