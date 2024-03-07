# Importing necessary libraries
import random
import datetime
import uuid
import json

# Defining parameters and data for simulation
usernames = [f'user{i}' for i in range(1, 101)]  # 100 sample usernames
ip_addresses = [f'192.168.1.{i}' for i in range(1, 255)]  # Sample IP addresses
auth_statuses = ['Success', 'Failed']  # Possible authentication statuses
error_messages = ['Invalid password', 'User not found', 'Account locked']  # Sample error messages
records = []  # List to store generated records

# Function to generate a random timestamp within the last 30 days
def random_timestamp():
    start_date = datetime.datetime.now() - datetime.timedelta(days=30)
    random_date = start_date + datetime.timedelta(seconds=random.randint(0, 2592000))  # 30 days in seconds
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

# Function to generate simulated authentication server logs
def generate_auth_logs(num_records=1000):
    for _ in range(num_records):
        timestamp = random_timestamp()
        username = random.choice(usernames)
        source_ip = random.choice(ip_addresses)
        auth_status = random.choice(auth_statuses)
        session_id = str(uuid.uuid4()) if auth_status == 'Success' else ''
        error_code = random.choice(error_messages) if auth_status == 'Failed' else ''
        logout_time = ''
        
        # For successful logins, set a random logout time (1 to 8 hours later)
        if auth_status == 'Success':
            logout_datetime = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=random.randint(1, 8))
            logout_time = logout_datetime.strftime('%Y-%m-%d %H:%M:%S')
        
        record = {
            'timestamp': timestamp,
            'username': username,
            'source_ip': source_ip,
            'auth_status': auth_status,
            'session_id': session_id,
            'error_message': error_code,
            'logout_time': logout_time
        }
        records.append(record)
    
    # Writing the generated records to a JSON file
    with open('auth_server_logs.json', 'w') as file:
        json.dump(records, file, indent=4)

# Note: Uncomment the following line to generate and save the logs
generate_auth_logs()
