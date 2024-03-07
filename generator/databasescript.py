# Import necessary libraries
from faker import Faker
import json
import os

# Initialize the Faker library
fake = Faker()

# Define the structure and generation function for Transaction Logs
def generate_transaction_logs(num_records):
    transaction_logs = []
    for _ in range(num_records):
        log = {
            "transaction_id": fake.uuid4(),
            "status": fake.random_element(elements=('success', 'fail')),
            "amount": fake.random_number(digits=5),
            "currency": fake.currency_code(),
            "timestamp": fake.iso8601()
        }
        transaction_logs.append(log)
    return transaction_logs

# Define the structure and generation function for Error Logs
def generate_error_logs(num_records):
    error_logs = []
    for _ in range(num_records):
        log = {
            "error_id": fake.uuid4(),
            "error_message": fake.sentence(),
            "severity": fake.random_element(elements=('low', 'medium', 'high')),
            "timestamp": fake.iso8601()
        }
        error_logs.append(log)
    return error_logs

# Define the structure and generation function for Query Logs
def generate_query_logs(num_records):
    query_logs = []
    for _ in range(num_records):
        log = {
            "query_id": fake.uuid4(),
            "query_text": fake.sentence(),
            "execution_time": fake.random_number(digits=2),  # in ms
            "timestamp": fake.iso8601()
        }
        query_logs.append(log)
    return query_logs

# Define the structure and generation function for Connection Logs
def generate_connection_logs(num_records):
    connection_logs = []
    for _ in range(num_records):
        log = {
            "connection_id": fake.uuid4(),
            "user": fake.user_name(),
            "status": fake.random_element(elements=('connected', 'disconnected')),
            "timestamp": fake.iso8601()
        }
        connection_logs.append(log)
    return connection_logs

# Define the structure and generation function for General Logs
def generate_general_logs(num_records):
    general_logs = []
    for _ in range(num_records):
        log = {
            "log_id": fake.uuid4(),
            "message": fake.sentence(),
            "level": fake.random_element(elements=('info', 'warning', 'error')),
            "timestamp": fake.iso8601()
        }
        general_logs.append(log)
    return general_logs

# Function to save logs to JSON files
def save_logs_to_file(logs, filename):
    with open(filename, 'w') as f:
        json.dump(logs, f, indent=4)

# Main function to generate and save logs
def generate_and_save_logs(num_records=1000):
    os.makedirs('generated_logs', exist_ok=True)  # Create directory for logs if it does not exist
    save_logs_to_file(generate_transaction_logs(num_records), 'generated_logs/transaction_logs.json')
    save_logs_to_file(generate_error_logs(num_records), 'generated_logs/error_logs.json')
    save_logs_to_file(generate_query_logs(num_records), 'generated_logs/query_logs.json')
    save_logs_to_file(generate_connection_logs(num_records), 'generated_logs/connection_logs.json')
    save_logs_to_file(generate_general_logs(num_records), 'generated_logs/general_logs.json')

# Uncomment the following line to generate and save logs
generate_and_save_logs()

