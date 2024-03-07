# Import necessary libraries
import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define functions to generate mock data for each category
def generate_asset_data(num_records):
    assets = []
    for _ in range(num_records):
        asset = {
            "ID": fake.uuid4(),
            "Name": fake.word(),
            "Type": random.choice(["Hardware", "Software", "Peripheral"]),
            "Location": fake.city(),
            "PurchaseDate": fake.date(),
            "Price": random.uniform(100, 10000)
        }
        assets.append(asset)
    return assets

def generate_device_data(num_records):
    devices = []
    for _ in range(num_records):
        device = {
            "DeviceID": fake.uuid4(),
            "Type": random.choice(["Laptop", "Desktop", "Tablet", "Phone"]),
            "Status": random.choice(["Active", "Inactive", "Decommissioned"]),
            "User": fake.name(),
            "IPAddress": fake.ipv4(),
            "LastMaintenanceDate": fake.date()
        }
        devices.append(device)
    return devices

def generate_traffic_data(num_records):
    traffic = []
    for _ in range(num_records):
        traffic_record = {
            "TrafficID": fake.uuid4(),
            "SourceIP": fake.ipv4(),
            "DestinationIP": fake.ipv4(),
            "Protocol": random.choice(["TCP", "UDP", "ICMP"]),
            "Port": random.randint(1, 65535),
            "Timestamp": fake.iso8601(),
            "DataTransferred": random.randint(1, 10000)  # in KB
        }
        traffic.append(traffic_record)
    return traffic

# Generate mock data
assets = generate_asset_data(1000)
devices = generate_device_data(1000)
traffic = generate_traffic_data(1000)

# Save data to JSON files
with open('/mnt/data/asset.json', 'w') as f:
    json.dump(assets, f)

with open('/mnt/data/device.json', 'w') as f:
    json.dump(devices, f)

with open('/mnt/data/traffic.json', 'w') as f:
    json.dump(traffic, f)

# Output file paths
#'/mnt/data/asset.json', '/mnt/data/device.json', '/mnt/data/traffic.json'
