import yaml
def read_and_modify_router_config(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            # Example modification: Change the IP of the first interface 
            if data['interfaces']:
                data['interfaces'][0]['ip'] = '10.10.10.1' # New IP address 
            return data
        except yaml.YAMLError as exc:
            print(exc)

def write_yaml(file_path, data): 
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

# Reading, modifying, and writing the router configuration
modified_config = read_and_modify_router_config('network_config.yml') 
write_yaml('modified_router_config.yml', modified_config)