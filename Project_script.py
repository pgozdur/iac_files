import argparse
import os
from git import Repo
from datetime import datetime
from pynautobot import api
from jinja2 import Environment, FileSystemLoader

def fetch_interfaces(nautobot, devices):
    interfaces = []
    for device in devices:
        device_interfaces = nautobot.dcim.interfaces.filter(device_id=device.id)
        interfaces.extend(device_interfaces)
    return interfaces

def fetch_devices(nautobot, role=None, location=None):
    if role and location:
        return nautobot.dcim.devices.filter(role=role, location=location)
    else:
        return nautobot.dcim.devices.all()

def generate_report(devices, filtered_devices, filtered_interfaces):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template.md')

    return template.render(devices=devices, filtered_devices=filtered_devices, filtered_interfaces=filtered_interfaces)

def write_report(report, filename, repo_path):
    file_path = os.path.join(repo_path, filename)
    with open(file_path, 'w') as f:
        f.write(report)

def commit_and_push(repo_path, filename):
    repo = Repo(repo_path)
    repo.git.add(filename)
    repo.git.commit('-m', f'Update {datetime.now().isoformat()}')
    repo.git.push()

def main(url, token, role, location, repo_path):
    nautobot = api(url=url, token=token)
    devices = fetch_devices(nautobot)
    filtered_devices = fetch_devices(nautobot, role, location)
    filtered_interfaces = fetch_interfaces(nautobot, filtered_devices)
    report = generate_report(devices, filtered_devices, filtered_interfaces)
    filename = f'report_{datetime.now().isoformat()}.md'
    write_report(report, filename, repo_path)
    commit_and_push(repo_path, filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate network documentation report.")
    parser.add_argument("role", help="Device role")
    parser.add_argument("location", help="Device location")
    parser.add_argument("repo_path", help="Path to the Git repository")

    BASE_URL = os.getenv('NAUTOBOT_URL')
    TOKEN = os.getenv('TOKEN')

    args = parser.parse_args()

    main(BASE_URL, TOKEN, args.role, args.location, args.repo_path)