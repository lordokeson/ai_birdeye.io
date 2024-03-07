# Import necessary libraries
from faker import Faker
import random

# Create an instance of the Faker class
fake = Faker()

# Define the number of records
num_records = 1000

# Initialize lists to hold log records for each category
access_logs = []
error_logs = []
referrer_logs = []
agent_logs = []
cookie_logs = []

# Define a list of sample HTTP methods
http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']

# Define a list of sample HTTP status codes
http_status_codes = [200, 301, 404, 500, 503]

# Define a list of sample error messages
error_messages = ['Not Found', 'Internal Server Error', 'Service Unavailable', 'Bad Gateway', 'Unauthorized']

# Generate data for each category
for _ in range(num_records):
    # Access log entry
    access_logs.append(f"{fake.ipv4()} - - [{fake.date_time()}] \"{random.choice(http_methods)} /{fake.uri_path()} HTTP/1.1\" {random.choice(http_status_codes)} {random.randint(200, 20000)}")
    
    # Error log entry
    error_logs.append(f"[{fake.date_time()}] [error] [client {fake.ipv4()}] {random.choice(error_messages)}: /{fake.uri_path()}, referer: {fake.url()}")
    
    # Referrer log entry
    referrer_logs.append(f"{fake.url()} - {fake.ipv4()} - [{fake.date_time()}] \"{random.choice(http_methods)} /{fake.uri_path()} HTTP/1.1\" {random.choice(http_status_codes)} {random.randint(200, 20000)} - \"{fake.url()}\"")
    
    # Agent log entry
    agent_logs.append(f"{fake.ipv4()} - - [{fake.date_time()}] \"{random.choice(http_methods)} /{fake.uri_path()} HTTP/1.1\" {random.choice(http_status_codes)} {random.randint(200, 20000)} \"{fake.user_agent()}\"")
    
    # Cookie log entry
    cookie_logs.append(f"{fake.ipv4()} - - [{fake.date_time()}] \"{fake.pystr(min_chars=10, max_chars=50)}\"")

# Save each category of logs to a separate file
with open("access_logs.txt", "w") as file:
    for record in access_logs:
        file.write(record + "\n")

with open("error_logs.txt", "w") as file:
    for record in error_logs:
        file.write(record + "\n")

with open("referrer_logs.txt", "w") as file:
    for record in referrer_logs:
        file.write(record + "\n")

with open("agent_logs.txt", "w") as file:
    for record in agent_logs:
        file.write(record + "\n")

with open("cookie_logs.txt", "w") as file:
    for record in cookie_logs:
        file.write(record + "\n")

# Return paths of the saved log files
["access_logs.txt", "error_logs.txt", "referrer_logs.txt", "agent_logs.txt", "cookie_logs.txt"]
