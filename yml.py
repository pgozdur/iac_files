import yaml
import json

with open('network_config.yml', 'r') as file:
    network_config = yaml.safe_load(file)

print(network_config)


network_data = {
    'switch': 'Switch1',
    'ports': [
        {'name': 'FastEthernet0/1', 'vlan': '10'},
        {'name': 'FastEthernet0/2', 'vlan': '20'}
    ]
}

with open('new_network_config.json', 'w') as file:
    json.dump(network_data, file, indent=4)
