# Import necessary libraries
import uuid
import random
from datetime import datetime, timedelta
import json

# Predefined lists for random selection
remediation_recommendations = [
    "Apply the latest patches",
    "Change default credentials",
    "Restrict network access",
    "Update software to the latest version",
    "Perform regular security audits"
]
device_names = ["Server-A", "Server-B", "Router-C", "Switch-D", "Firewall-E"]
attack_resources = ["/admin", "/login.php", "config.xml", "database.sql", "/api/user"]
attack_methods = ["SQL Injection", "Cross Site Scripting", "Denial of Service", "Phishing", "Ransomware"]
tags = ["urgent", "review required", "external", "internal", "authentication", "encryption"]

# Function to generate a single record
def generate_record():
    # Generate data for each field
    record_id = str(uuid.uuid4())
    cvss_score = round(random.uniform(0, 10), 1)
    recommendation = random.choice(remediation_recommendations)
    timestamp = (datetime.now() - timedelta(days=random.randint(0, 365), minutes=random.randint(0, 1440))).isoformat()
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    device_name = random.choice(device_names)
    resource = random.choice(attack_resources)
    method = random.choice(attack_methods)
    severity = "Low" if cvss_score <= 3 else "Medium" if cvss_score <= 6 else "High" if cvss_score <= 8 else "Critical"
    record_tags = random.sample(tags, k=2)  # Select 2 random tags

    # Combine data into a record
    record = {
        "ID": record_id,
        "CVSS Score": cvss_score,
        "Remediation Recommendation": recommendation,
        "Timestamp": timestamp,
        "IP Address": ip_address,
        "Device Name": device_name,
        "Attack Resources": resource,
        "Attack Method": method,
        "Severity Level": severity,
        "Tags": record_tags
    }
    return record

# Generate 1000 records
records = [generate_record() for _ in range(1000)]

# Save to a file
file_name = 'vulnerability_logs.json'
with open(file_name, 'w') as file:
    json.dump(records, file, indent=4)

# Return the path of the file for user to download
file_name
