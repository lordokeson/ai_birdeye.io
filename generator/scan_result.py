# Importing necessary libraries
from faker import Faker
import json
from datetime import datetime

# Initialize the Faker library
fake = Faker()

# Function to generate fake data for Vulnerability Scan Results
def generate_vulnerability_scan_results(num_records):
    results = []
    for _ in range(num_records):
        result = {
            "scan_id": fake.uuid4(),
            "resource_id": fake.uuid4(),
            "vulnerability_type": fake.word(),
            "severity": fake.random_element(elements=("Low", "Medium", "High", "Critical")),
            "description": fake.text(max_nb_chars=200),
            "recommendation": fake.text(max_nb_chars=100),
            "date_detected": fake.date_time_between(start_date="-2y", end_date="now").isoformat()
        }
        results.append(result)
    return results

# Function to generate fake data for Resource Information
def generate_resource_info(num_records):
    resources = []
    for _ in range(num_records):
        resource = {
            "resource_id": fake.uuid4(),
            "resource_type": fake.random_element(elements=("Server", "Database", "Storage", "Network Device")),
            "location": fake.random_element(elements=("On-prem", "Cloud")),
            "ip_address": fake.ipv4(),
            "operating_system": fake.random_element(elements=("Windows Server 2019", "Ubuntu 20.04", "Red Hat Enterprise Linux 8")),
            "status": fake.random_element(elements=("Active", "Inactive", "Decommissioned"))
        }
        resources.append(resource)
    return resources

# Function to generate fake data for Server Logs
def generate_server_logs(num_records):
    logs = []
    for _ in range(num_records):
        log = {
            "log_id": fake.uuid4(),
            "resource_id": fake.uuid4(),
            "timestamp": fake.date_time_between(start_date="-2y", end_date="now").isoformat(),
            "log_level": fake.random_element(elements=("INFO", "WARNING", "ERROR", "DEBUG")),
            "message": fake.sentence(nb_words=10)
        }
        logs.append(log)
    return logs

# Function to generate fake data for File System Information
def generate_file_system_info(num_records):
    file_info = []
    for _ in range(num_records):
        file = {
            "file_id": fake.uuid4(),
            "resource_id": fake.uuid4(),
            "file_path": fake.file_path(depth=5),
            "file_size": fake.random_int(min=0, max=1024),  # File size in KB
            "file_type": fake.file_extension(),
            "last_modified": fake.date_time_between(start_date="-2y", end_date="now").isoformat()
        }
        file_info.append(file)
    return file_info

# Function to save data to a JSON file
def save_data_to_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

#Uncomment below lines to generate and save the data. Temporarily commented for code review.
vulnerability_data = generate_vulnerability_scan_results(1000)
save_data_to_json('vulnerability_scan_results.json', vulnerability_data)

resource_data = generate_resource_info(1000)
save_data_to_json('resource_information.json', resource_data)

server_log_data = generate_server_logs(1000)
save_data_to_json('server_logs.json', server_log_data)

file_system_data = generate_file_system_info(1000)
save_data_to_json('file_system_information.json', file_system_data)
