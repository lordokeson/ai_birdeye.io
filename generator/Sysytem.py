# Import necessary libraries
from faker import Faker
import json

# Initialize the Faker library
fake = Faker()

# Define a function to generate mock access logs
def generate_access_logs(n):
    logs = []
    for _ in range(n):
        log = {
            'timestamp': fake.iso8601(),
            'ip_address': fake.ipv4(),
            'request_method': fake.http_method(),
            'status_code': fake.random_element(elements=[200, 301, 404, 500]),
            'user_agent': fake.user_agent()
        }
        logs.append(log)
    return logs

# Define a function to generate mock error logs
def generate_error_logs(n):
    logs = []
    for _ in range(n):
        log = {
            'timestamp': fake.iso8601(),
            'error_level': fake.random_element(elements=['ERROR', 'WARNING', 'NOTICE']),
            'message': fake.sentence(),
        }
        logs.append(log)
    return logs

# Define a function to generate mock authentication logs
def generate_authentication_logs(n):
    logs = []
    for _ in range(n):
        log = {
            'timestamp': fake.iso8601(),
            'user_id': fake.user_name(),
            'action': fake.random_element(elements=['login_success', 'login_failure']),
            'source_ip': fake.ipv4()
        }
        logs.append(log)
    return logs

# Define a function to generate mock transaction logs
def generate_transaction_logs(n):
    logs = []
    for _ in range(n):
        log = {
            'timestamp': fake.iso8601(),
            'transaction_id': fake.uuid4(),
            'status': fake.random_element(elements=['completed', 'failed', 'pending']),
            'amount': fake.random_number(digits=5)
        }
        logs.append(log)
    return logs

# Define a function to generate mock service logs
def generate_service_logs(n):
    logs = []
    for _ in range(n):
        log = {
            'timestamp': fake.iso8601(),
            'service_name': fake.word(),
            'status': fake.random_element(elements=['running', 'stopped', 'error']),
            'message': fake.sentence()
        }
        logs.append(log)
    return logs

#Uncomment the following lines to generate and save logs to files
with open('access_logs.json', 'w') as f:
    json.dump(generate_access_logs(1000), f, indent=4)

with open('error_logs.json', 'w') as f:
    json.dump(generate_error_logs(1000), f, indent=4)

with open('authentication_logs.json', 'w') as f:
    json.dump(generate_authentication_logs(1000), f, indent=4)

with open('transaction_logs.json', 'w') as f:
    json.dump(generate_transaction_logs(1000), f, indent=4)

with open('service_logs.json', 'w') as f:
    json.dump(generate_service_logs(1000), f, indent=4)
