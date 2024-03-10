import os
from pynautobot import api

BASE_URL = os.getenv('NAUTOBOT_URL')
TOKEN = os.getenv('TOKEN')


nautobot = api(url=BASE_URL, token=TOKEN)

# Define the new VRF details

vrf_data = {
    'name': 'Customer_1',
    'rd': '65000:1',
    'status': "Active", 
    'namespace': "Global",
}

# Create the VRF
customer_1_vrf = nautobot.ipam.vrfs.create(**vrf_data)

# Associate the VRF with Spine devices in London
print("VRF 'Customer_1' created.")
