import json
import random
from datetime import datetime, timedelta

# Define the function to generate a single log record
def generate_log_entry(log_level):
    timestamp = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d %H:%M:%S')
    message = f"This is a {log_level} message."
    process_id = random.randint(1000, 9999)
    thread_id = random.randint(1000, 9999)
    return {
        "timestamp": timestamp,
        "log_level": log_level,
        "message": message,
        "process_id": process_id,
        "thread_id": thread_id
    }

# Define the function to generate all log entries
def generate_log_entries():
    log_levels = ["INFO", "WARNING", "ERROR"]
    log_entries = {level: [] for level in log_levels}  # Dictionary to store logs by level
    
    for level in log_levels:
        for _ in range(1000):  # Generate 1000 log entries for each level
            log_entries[level].append(generate_log_entry(level))
    
    return log_entries

# Generate all log entries
all_log_entries = generate_log_entries()

# Saving the generated log entries to a JSON file
file_name = '/mnt/data/kernel_server_logs.json'
with open(file_name, 'w') as json_file:
    json.dump(all_log_entries, json_file, indent=4)
