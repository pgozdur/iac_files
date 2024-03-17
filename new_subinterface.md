# Create New Subinterface Script

This script is used to add a new subinterface to a device in Nautobot. It also checks if the subinterface or VLAN already exists and handles these cases appropriately.

## Usage

The script is run from the command line with the following arguments:

- `nautobot`: The Nautobot instance to connect to.
- `device`: The device to which the subinterface should be added.
- `interface_name`: The name of the interface to which the subinterface should be added.
- `vlan`: The VLAN ID for the new subinterface.

## Code

Here is the full script:

```python
import argparse
from pynautobot import api
import os

def add_sub_interface(nautobot, device, interface_name, vlan):
    # Fetch the parent interface
    parent_interface = nautobot.dcim.interfaces.get(device_id=device.id, name=interface_name)

    # Define the new subinterface details
    subinterface_data = {
        'device': device.id,
        'name': f'{interface_name}.{vlan}',
        'type': 'virtual',
        'status': 'Active',
        'parent_interface': parent_interface.id,
    }

    # Create the subinterface
    # Check if the subinterface already exists
    existing_subinterface = nautobot.dcim.interfaces.get(device_id=device.id, name=subinterface_data['name'])

    # If the subinterface doesn't exist, create it
    if existing_subinterface is None:
        subinterface = nautobot.dcim.interfaces.create(**subinterface_data)
        print(f"Subinterface {subinterface.name} created.")
    else:
        subinterface = existing_subinterface
        print(f"Subinterface {existing_subinterface.name} already exists.")

    # Check if the VLAN already exists
    existing_vlan = nautobot.ipam.vlans.get(vid=vlan)

    # If the VLAN doesn't exist, create it
    if existing_vlan is None:
        vlan_data = {
            'vid': vlan,
            'name': f'VLAN {vlan}',
            'status': 'Active',
            'location': device.location.id,
        }
        vlan = nautobot.ipam.vlans.create(**vlan_data)
        subinterface.tagged_vlans = [vlan.id]
        subinterface.mode = "tagged"
        subinterface.save()

        print(f"VLAN {vlan.vid} created.")
        print(f"VLAN {vlan.vid} assigned to interface {subinterface.name} ")