# Importing necessary libraries for mock data generation
import json
import random
import ipaddress
from datetime import datetime, timedelta

# Function to generate a random IP address
def generate_ip():
    return str(ipaddress.ip_address(random.randint(0, 2**32 - 1)))

# Function to generate random log records for each category
def generate_firewall_logs(num_records):
    logs = {'TrafficLogs': [], 'ThreatLogs': [], 'SystemLogs': [], 'AuthenticationLogs': [], 'VPNLogs': []}
    protocols = ['TCP', 'UDP', 'ICMP']
    threat_types = ['Malware', 'Intrusion', 'Info Leak']
    event_types = ['Configuration Change', 'System Start', 'System Stop']
    users = ['user1', 'user2', 'user3', 'admin']
    actions = ['Allow', 'Deny', 'Drop']
    severity_levels = ['Low', 'Medium', 'High']
    auth_statuses = ['Success', 'Failure']

    for _ in range(num_records):
        # Generating Traffic Logs
        logs['TrafficLogs'].append({
            'SourceIP': generate_ip(),
            'DestinationIP': generate_ip(),
            'SourcePort': random.randint(1024, 65535),
            'DestinationPort': random.randint(1024, 65535),
            'Protocol': random.choice(protocols),
            'Action': random.choice(actions)
        })

        # Generating Threat Logs
        logs['ThreatLogs'].append({
            'Timestamp': str(datetime.now() - timedelta(minutes=random.randint(0, 60))),
            'ThreatType': random.choice(threat_types),
            'Severity': random.choice(severity_levels),
            'SourceIP': generate_ip(),
            'DestinationIP': generate_ip()
        })

        # Generating System Logs
        logs['SystemLogs'].append({
            'Timestamp': str(datetime.now() - timedelta(minutes=random.randint(0, 60))),
            'EventType': random.choice(event_types),
            'User': random.choice(users),
            'Description': 'Sample description for event.'
        })

        # Generating Authentication Logs
        logs['AuthenticationLogs'].append({
            'Timestamp': str(datetime.now() - timedelta(minutes=random.randint(0, 60))),
            'User': random.choice(users),
            'SourceIP': generate_ip(),
            'Status': random.choice(auth_statuses)
        })

        # Generating VPN Logs
        start_time = datetime.now() - timedelta(minutes=random.randint(0, 60))
        end_time = start_time + timedelta(minutes=random.randint(1, 60))
        logs['VPNLogs'].append({
            'StartTime': str(start_time),
            'EndTime': str(end_time),
            'ClientIP': generate_ip(),
            'User': random.choice(users),
            'DataTransmitted': random.randint(1000, 1000000)  # bytes
        })

    return logs

# Generate mock data for 1000 records of each category
mock_data = generate_firewall_logs(1000)

# Saving the mock data to a JSON file
with open('/mnt/data/firewall_logs.json', 'w') as file:
    json.dump(mock_data, file, indent=4)

# Return the path of the generated file for the user to download
'/mnt/data/firewall_logs.json'
