import csv
import json
import logging
import os
import random
from datetime import datetime, timedelta

def generate_random_log_events(num_events=1000):
    log_events = []

    for _ in range(num_events):
        username = generate_random_username()
        email = generate_random_email(username)
        timestamp = generate_random_timestamp()
        ip_address = generate_random_ip_address()
        success_failure = random.choice(['Success', 'Failure'])
        intrusion_alert = random.choice(['Intrusion Detected', 'No Intrusion'])

        log_event = f'{timestamp} | {username} | {ip_address} | {email} | {success_failure} | {intrusion_alert}'
        log_events.append(log_event)

    return log_events

def generate_random_username():
    prefixes = ['user', 'admin', 'guest']
    suffix = random.randint(100, 999)
    return random.choice(prefixes) + str(suffix)

def generate_random_email(username):
    domains = ['example.com', 'company.com', 'test.org']
    return f'{username}@{random.choice(domains)}'

def generate_random_timestamp():
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

def generate_random_ip_address():
    return f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'

def save_log_events_to_file(log_events, filename='ids.log'):
    with open(filename, 'w', newline='') as file:
        for log_event in log_events:
            file.write(log_event + '\n')

if __name__ == '__main__':
    log_events = generate_random_log_events()
    save_log_events_to_file(log_events)
