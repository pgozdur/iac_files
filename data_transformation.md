# Data Transformation Script Documentation

This Python script is used for reading, modifying, and writing YAML files. It's particularly useful for modifying router configurations.

## Dependencies

The script uses the PyYAML library. You can install it with pip:

```bash
pip install pyyaml
```

## Functions

The script contains two main functions:

### `read_and_modify_router_config(file_path)`

This function reads a YAML file from the provided file path, modifies the data, and returns the modified data.

The function expects the YAML file to contain a dictionary with a key 'interfaces' that maps to a list of interfaces. Each interface is a dictionary that should contain a key 'ip' that maps to the IP address of the interface.

The function modifies the IP address of the first interface to '10.10.10.1'.

If the YAML file cannot be parsed, the function prints the error and returns None.

```python
def read_and_modify_router_config(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            if data['interfaces']:
                data['interfaces'][0]['ip'] = '10.10.10.1'
            return data
        except yaml.YAMLError as exc:
            print(exc)
```

### `write_yaml(file_path, data)`

This function writes the provided data to a YAML file at the provided file path. The keys in the YAML file are not sorted.

```python
def write_yaml(file_path, data):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, sort_keys=False)
```

## Usage

The script reads a router configuration from 'network_config.yml', modifies the configuration, and writes the modified configuration to 'modified_router_config.yml'.

```python
modified_config = read_and_modify_router_config('network_config.yml')
write_yaml('modified_router_config.yml', modified_config)
```

You can modify the script to read from and write to different files, or to modify the configuration in different ways.