# Import required libraries
import random
import csv
from datetime import datetime, timedelta

# Constants for data generation
DOMAINS = ["example.com", "mail.com", "server.net"]
STATUS = ["sent", "failed", "deferred"]
SUBJECT_WORDS = ["Urgent", "Meeting", "Report", "Invoice", "Reminder"]
MAX_EMAIL_SIZE = 10485760  # 10 MB in bytes
NUM_RECORDS = 1000

# Function to generate a random email address
def generate_email():
    return f"user{random.randint(1, 1000)}@{random.choice(DOMAINS)}"

# Function to generate a random subject line
def generate_subject():
    return f"{random.choice(SUBJECT_WORDS)}: Important Notice {random.randint(1, 100)}"

# Function to generate a random timestamp within the last 30 days
def generate_timestamp():
    return datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))

# Function to generate a random size for email
def generate_size():
    return random.randint(1, MAX_EMAIL_SIZE)

# Function to generate a single record
def generate_record():
    return {
        "timestamp": generate_timestamp(),
        "sender": generate_email(),
        "recipient": generate_email(),
        "subject": generate_subject(),
        "status": random.choice(STATUS),
        "size": generate_size()
    }

# Function to generate multiple records and save them to a CSV file
def generate_and_save_records(filename, num_records):
    records = [generate_record() for _ in range(num_records)]
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["timestamp", "sender", "recipient", "subject", "status", "size"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

# Uncomment the below line to generate and save 1000 records to mail_logs.csv
generate_and_save_records("mail_logs.csv", NUM_RECORDS)
