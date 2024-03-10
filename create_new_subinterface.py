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
    else:
        vlan = existing_vlan
        subinterface.tagged_vlans = [vlan.id]
        subinterface.mode = "tagged"
        subinterface.save()
        print(f"VLAN {vlan.vid} already exists.")
        print(f"VLAN {vlan.vid} assigned to interface {subinterface.name} ")

def choose_interface(interfaces):
    print("Interfaces:")
    for i, interface in enumerate(interfaces, start=1):
        print(f"{i}. {interface.name}")

    choice = int(input("Enter the number of the interface you want to use: ")) - 1
    return interfaces[choice].name

def main(url, token, location, device_role, vlan):
    nautobot = api(url=url, token=token)

    # Fetch devices by location and role
    devices = nautobot.dcim.devices.filter(location=location, role=device_role)

    for device in devices:
        # Fetch the interfaces for the device
        interfaces = nautobot.dcim.interfaces.filter(device_id=device.id)

        # Check if the device has any interfaces
        if interfaces:
            interface_name = choose_interface(interfaces)  # Get user input for interface
            add_sub_interface(nautobot, device, interface_name, vlan)
        else:
            print(f"No interfaces found for device {device.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add sub-interface to spine switches.")
    parser.add_argument("location", help="Location name of the devices")
    parser.add_argument("device_role", help="Device role, e.g., 'spine'")
    parser.add_argument("vlan", type=int, help="VLAN number for the sub-interface")

    # These could be arguments, environment variables, or hardcoded values
    BASE_URL = os.getenv('NAUTOBOT_URL')
    TOKEN = os.getenv('TOKEN')

    args = parser.parse_args()

    main(BASE_URL, TOKEN, args.location, args.device_role, args.vlan)