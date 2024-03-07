# Required libraries
import random
import datetime
import json

# Constants and setups
USER_IDS = range(1, 101)  # Assuming 100 unique users
EVENT_TYPES = ['login', 'logout', 'error', 'warning', 'info']
STATUS_CODES = [200, 400, 401, 403, 404, 500]
RESOURCE_TYPES = ['CPU', 'Memory', 'Disk']
OPERATION_TYPES = ['read', 'write', 'execute']
IP_ADDRESSES = [f"192.168.1.{i}" for i in range(1, 256)]  # Simplified example

# Function to generate a single record
def generate_record():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = random.choice(USER_IDS)
    event_type = random.choice(EVENT_TYPES)
    ip_address = random.choice(IP_ADDRESSES)
    status_code = random.choice(STATUS_CODES)
    error_message = f"Error {status_code}" if status_code >= 400 else ""
    resource_usage = {res: random.randint(1, 100) for res in RESOURCE_TYPES}
    session_id = f"sess_{random.randint(1, 10000)}"
    file_path = f"/path/to/file_{random.randint(1, 100)}.txt"
    operation_detail = random.choice(OPERATION_TYPES)
    
    # Constructing the log record as a dictionary
    log_record = {
        "timestamp": timestamp,
        "user_id": user_id,
        "event_type": event_type,
        "ip_address": ip_address,
        "status_code": status_code,
        "error_message": error_message,
        "resource_usage": resource_usage,
        "session_id": session_id,
        "file_path": file_path,
        "operation_detail": operation_detail
    }
    return log_record

# Generating 1000 records for each category and write to a file
def generate_log_file(filename="log_records.json"):
    records = [generate_record() for _ in range(1000)]
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

# Uncomment the following line to generate the log file
generate_log_file()
