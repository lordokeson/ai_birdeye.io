
# Recent
# Security Report Generation using Python
# In-depth Review and Strong Recommendation for Application Security Engineer CV
# 10 Scenario-Based Questions and Answers for a Cloud System Engineer
# Quincy, MA, USA
# Based on your places (Home) • Update location 
# Conversation with Bard
# profile picture
# You have been tasked with generating a comprehensive security report that combines data from three sources:
# Vulnerability Scan Data: A CSV file named vulnerabilities.csv containing vulnerability details, including CVSS scores (column named cvss_score).
# Asset Inventory: A JSON file named assets.json containing asset information, including asset names, IP addresses, and criticality levels (property named criticality).
# Log Files: A directory named logs containing various log files with potential security events.
# Your task is to create a Python script that:
# Parses the vulnerability scan data and extracts vulnerabilities with a CVSS score of 7.0 or higher.
# Parses the asset inventory and identifies assets with a criticality level of "High" or "Critical".
# Analyzes the log files for potential security events (e.g., failed login attempts, intrusion alerts).
# Combines the extracted data into a single report, highlighting vulnerabilities in critical assets and relevant security events.
# Formats the report in a clear and readable manner (e.g., using tables and Markdown).

# file name is 
# vulnerabilities.csv

# file data structure of vulnerabilities.csv is
# id,hostname,ip_address,vulnerability,cvss_score
# 1,server1,192.168.1.10,SQL injection,7.8
# 2,server2,10.0.0.2,Open SSH weak ciphers,6.5
# 3,workstation1,172.16.0.5,Missing security updates,5.2
# 4,workstation2,10.0.0.5,Unnecessary services running,4.8
# 5,server3,192.168.1.20,Cross-site scripting,8.3

# file name is
# assets.json

# file data structure of assets.json is
# [
#     {
#       "name": "Server 1",
#       "ip_address": "192.168.1.10",
#       "criticality": "Critical"
#     },
#     {
#       "name": "Server 2",
#       "ip_address": "192.168.1.11",
#       "criticality": "High"
#     },
#     {
#       "name": "Workstation 1",
#       "ip_address": "192.168.1.12",
#       "criticality": "Medium"
#     },
#     {
#       "name": "Database Server",
#       "ip_address": "192.168.1.13",
#       "criticality": "Critical"
#     },
#     {
#       "name": "Web Server",
#       "ip_address": "192.168.1.14",
#       "criticality": "Low"
#     }
# ]

# file name is 
# login_attempts.log

# file data structure of login_attempts.log is
# 2024-01-29 12:01:01 | user123 | Success
# 2024-01-29 12:02:15 | admin456 | Failure
# 2024-01-29 12:03:30 | guest789 | Success
# 2024-01-29 12:04:45 | user123 | Failure
# 2024-01-29 12:05:59 | john_doe | Success

# file name is 
# intrusion_alerts.log

# file data structure of intrusion_alerts.log is 
# 2024-01-29 12:01:01 | user123 | Success
# 2024-01-29 12:02:15 | admin456 | Failure
# 2024-01-29 12:03:30 | guest789 | Success
# 2024-01-29 12:04:45 | user123 | Failure
# 2024-01-29 12:05:59 | john_doe | Success

# the log files are all in the same directory called logs
# the log directory, assets.json file and vulnerabilities.csv file are in the same directory
# Here's the Python script to generate the comprehensive security report:


# import csv
# import json
# import os
# import re

# # Function to parse vulnerabilities from CSV
# def parse_vulnerabilities(csv_file):
#     vulnerabilities = []
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             if float(row['cvss_score']) >= 7.0:
#                 vulnerabilities.append(row)
#     return vulnerabilities

# # Function to parse assets from JSON
# def parse_assets(json_file):
#     with open(json_file, 'r') as file:
#         assets = json.load(file)
#     critical_assets = [asset for asset in assets if asset['criticality'] in ('High', 'Critical')]
#     return critical_assets

# # Function to analyze log files
# def analyze_logs(log_directory):
#     security_events = []
#     for filename in os.listdir(log_directory):
#         file_path = os.path.join(log_directory, filename)
#         with open(file_path, 'r') as file:
#             for line in file:
#                 match = re.search(r'\|\s*(Failure|Success)\s*\|$', line)
#                 if match:
#                     security_events.append({
#                         'timestamp': line.split('|')[0],
#                         'event_type': match.group(1),
#                         'log_file': filename
#                     })
#     return security_events

# # Function to generate the report
# def generate_report(vulnerabilities, critical_assets, security_events):
#     report = f"# Security Report\n\n"

#     # Vulnerabilities
#     if vulnerabilities:
#         report += "## Vulnerabilities\n\n"
#         report += "| ID | Hostname | IP Address | Vulnerability | CVSS Score |\n"
#         report += "|---|---|---|---|---|\n"
#         for vulnerability in vulnerabilities:
#             report += f"| {vulnerability['id']} | {vulnerability['hostname']} | {vulnerability['ip_address']} | {vulnerability['vulnerability']} | {vulnerability['cvss_score']} |\n"

#     # Critical Assets
#     if critical_assets:
#         report += "## Critical Assets\n\n"
#         report += "| Name | IP Address | Criticality |\n"
#         report += "|---|---|---|\n"
#         for asset in critical_assets:
#             report += f"| {asset['name']} | {asset['ip_address']} | {asset['criticality']} |\n"

#     # Security Events
#     if security_events:
#         report += "## Security Events\n\n"
#         report += "| Timestamp | Event Type | Log File |\n"
#         report += "|---|---|---|\n"
#         for event in security_events:
#             report += f"| {event['timestamp']} | {event['event_type']} | {event['log_file']} |\n"

#     return report

# # Main execution
# vulnerabilities = parse_vulnerabilities('vulnerabilities.csv')
# critical_assets = parse_assets('assets.json')
# security_events = analyze_logs('logs')
# report = generate_report(vulnerabilities, critical_assets, security_events)

# import csv
# import json
# import os
# import re

# # Function to parse vulnerabilities CSV file
# def parse_vulnerabilities(csv_file):
#     vulnerabilities = []
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             if float(row['cvss_score']) >= 7.0:
#                 vulnerabilities.append(row)
#     return vulnerabilities

# # Function to parse asset inventory JSON file
# def parse_assets(json_file):
#     with open(json_file, 'r') as file:
#         assets = json.load(file)
#     critical_assets = [asset for asset in assets if asset['criticality'] in ('High', 'Critical')]
#     return critical_assets

# # Function to analyze log files
# def analyze_logs(log_dir):
#     security_events = []
#     for log_file in os.listdir(log_dir):
#         with open(os.path.join(log_dir, log_file), 'r') as file:
#             for line in file:
#                 match = re.search(r'\b(Failure|Alert)\b', line)
#                 if match:
#                     security_events.append({'log_file': log_file, 'event': line.strip()})
#     return security_events

# # Function to generate the security report
# def generate_report(vulnerabilities, critical_assets, security_events):
#     report = f"# Security Report\n\n## Vulnerabilities (CVSS Score >= 7.0)\n\n"
#     report += "| ID | Hostname | IP Address | Vulnerability | CVSS Score |\n"
#     report += "|---|---|---|---|---|\n"
#     for vulnerability in vulnerabilities:
#         report += f"| {vulnerability['id']} | {vulnerability['hostname']} | {vulnerability['ip_address']} | {vulnerability['vulnerability']} | {vulnerability['cvss_score']} |\n"

#     report += "\n## Critical Assets with Vulnerabilities\n\n"
#     for asset in critical_assets:
#         vulnerable = False
#         for vulnerability in vulnerabilities:
#             if asset['ip_address'] == vulnerability['ip_address']:
#                 report += f"- **{asset['name']}** ({asset['ip_address']}) has the following vulnerabilities:\n"
#                 report += f"  - {vulnerability['vulnerability']} (CVSS Score: {vulnerability['cvss_score']})\n"
#                 vulnerable = True
#         if not vulnerable:
#             report += f"- **{asset['name']}** ({asset['ip_address']}) has no critical vulnerabilities.\n"

#     report += "\n## Security Events\n\n"
#     for event in security_events:
#         report += f"- **{event['log_file']}:** {event['event']}\n"

#     return report

# # Main execution
# vulnerabilities_csv = 'vulnerabilities.csv'
# assets_json = 'assets.json'
# log_dir = 'logs'

# vulnerabilities = parse_vulnerabilities(vulnerabilities_csv)
# critical_assets = parse_assets(assets_json)
# security_events = analyze_logs(log_dir)

# report = generate_report(vulnerabilities, critical_assets, security_events)

# # Save report to file
# with open('security_report.md', 'w') as f:
#     f.write(report)

# # Print or save the report
# print(report)


import numpy as np
import matplotlib.pyplot as plt  
import csv
import json
import os
import re

# Function to parse vulnerabilities CSV file
def parse_vulnerabilities(csv_file):
    vulnerabilities = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if float(row['cvss_score']) >= 7.0:
                vulnerabilities.append(row)
    return vulnerabilities

# Function to parse asset inventory JSON file
def parse_assets(json_file):
    with open(json_file, 'r') as file:
        assets = json.load(file)
    critical_assets = [asset for asset in assets if asset['criticality'] in ('High', 'Critical')]
    return critical_assets

# Function to analyze log files
def analyze_logs(log_dir, log_file_name=None):
    security_events = []
    if log_file_name:
        log_file_path = os.path.join(log_dir, log_file_name)
        try:
            with open(log_file_path, 'r') as file:
                for line in file:
                    match = re.search(r'\b(Failure|Alert)\b', line)
                    if match:
                        security_events.append({'log_file': log_file_name, 'event': line.strip()})
        except FileNotFoundError:
            print(f"Error: File not found: {log_file_path}")
    else:
        if os.path.isdir(log_dir):
            for log_file in os.listdir(log_dir):
                log_file_path = os.path.join(log_dir, log_file)
                if os.path.isfile(log_file_path):
                    try:
                        with open(log_file_path, 'r') as file:
                            for line in file:
                                match = re.search(r'\b(Failure|Alert)\b', line)
                                if match:
                                    security_events.append({'log_file': log_file, 'event': line.strip()})
                    except FileNotFoundError:
                        print(f"Error: File not found: {log_file_path}")
        else:
            print(f"Error: {log_dir} is not a directory.")

    return security_events


# Function to generate the security report
def generate_report(vulnerabilities, critical_assets, security_events, login_attempts, intrusion_alerts):
    report = "# Security Report\n\n## Vulnerabilities (CVSS Score >= 7.0)\n\n"
    report += "| ID | Hostname | IP Address | Vulnerability | CVSS Score |\n"
    report += "|---|---|---|---|---|\n"
    for vulnerability in vulnerabilities:
        report += f"| {vulnerability['id']} | {vulnerability['hostname']} | {vulnerability['ip_address']} | {vulnerability['vulnerability']} | {vulnerability['cvss_score']} |\n"

    report += "\n## Critical Assets with Vulnerabilities\n\n"
    for asset in critical_assets:
        vulnerable = False
        for vulnerability in vulnerabilities:
            if asset['ip_address'] == vulnerability['ip_address']:
                report += f"- **{asset['name']}** ({asset['ip_address']}) has the following vulnerabilities:\n"
                report += f"  - {vulnerability['vulnerability']} (CVSS Score: {vulnerability['cvss_score']})\n"
                vulnerable = True
        if not vulnerable:
            report += f"- **{asset['name']}** ({asset['ip_address']}) has no critical vulnerabilities.\n"

    report += "\n## Security Events\n\n"
    for event in security_events:
        report += f"- **{event['log_file']}:** {event['event']}\n"

    report += "\n## Login Attempts\n\n"
    for attempt in login_attempts:
        report += f"- **Login Attempts ({attempt['log_file']}):** {attempt['event']}\n"

    report += "\n## Intrusion Alerts\n\n"
    for alert in intrusion_alerts:
        report += f"- **Intrusion Alert ({alert['log_file']}):** {alert['event']}\n"

    return report

# Main execution
vulnerabilities_csv = 'vulnerabilities.csv'
assets_json = 'assets.json'
log_dir = 'logs'

vulnerabilities = parse_vulnerabilities(vulnerabilities_csv)
critical_assets = parse_assets(assets_json)
security_events = analyze_logs(log_dir)

# Analyze login attempts log files
login_attempts = analyze_logs(os.path.join(log_dir, 'login_attempts.log'))

# Analyze intrusion alerts log files
intrusion_alerts = analyze_logs(os.path.join(log_dir, 'intrusion_alerts.log'))

report = generate_report(vulnerabilities, critical_assets, security_events, login_attempts, intrusion_alerts)

# Save report to file
with open('security_report.md', 'w') as f:
    f.write(report)

# Print or save the report
print(report)

# Visualization (Example using matplotlib)
labels = ['Vulnerabilities', 'Critical Assets', 'Security Events', 'Login Attempts', 'Intrusion Alerts']
sizes = [len(vulnerabilities), len(critical_assets), len(security_events), len(login_attempts), len(intrusion_alerts)]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
explode = (0.1, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()

