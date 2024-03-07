# Security Report

## Vulnerabilities (CVSS Score >= 7.0)

| ID | Hostname | IP Address | Vulnerability | CVSS Score |
|---|---|---|---|---|
| 1 | server1 | 192.168.1.10 | SQL injection | 7.8 |
| 5 | server3 | 192.168.1.20 | Cross-site scripting | 8.3 |
| 8 | workstation3 | 172.16.0.10 | LDAP injection | 7.1 |
| 10 | router1 | 10.0.0.15 | Buffer overflow | 9.0 |
| 13 | workstation4 | 172.16.0.15 | Brute force attack vulnerability | 7.4 |
| 15 | firewall1 | 10.0.0.25 | Cross-Site Request Forgery (CSRF) | 8.1 |
| 17 | server8 | 10.0.0.18 | Denial of Service (DoS) susceptibility | 7.9 |
| 19 | server9 | 192.168.1.50 | Session fixation | 8.6 |
| 20 | router2 | 10.0.0.30 | SQL injection | 7.2 |
| 22 | server10 | 10.0.0.22 | Cross-site scripting | 8.9 |
| 27 | server12 | 10.0.0.28 | LDAP injection | 7.0 |
| 29 | server13 | 192.168.1.70 | Buffer overflow | 8.5 |
| 32 | server14 | 10.0.0.32 | Brute force attack vulnerability | 7.3 |
| 34 | server15 | 192.168.1.80 | Cross-Site Request Forgery (CSRF) | 8.0 |
| 36 | device7 | 192.168.2.45 | Denial of Service (DoS) susceptibility | 7.8 |
| 38 | workstation9 | 172.16.0.40 | Session fixation | 8.4 |
| 39 | server17 | 192.168.1.90 | SQL injection | 7.5 |
| 41 | device8 | 192.168.2.50 | Cross-site scripting | 8.7 |
| 46 | device9 | 192.168.2.55 | LDAP injection | 7.2 |
| 48 | workstation11 | 172.16.0.50 | Buffer overflow | 8.2 |

## Critical Assets with Vulnerabilities

- **Server 1** (192.168.1.10) has the following vulnerabilities:
  - SQL injection (CVSS Score: 7.8)
- **Server 2** (192.168.1.11) has no critical vulnerabilities.
- **Database Server** (192.168.1.13) has no critical vulnerabilities.
- **Backup Server** (192.168.1.15) has no critical vulnerabilities.
- **Router** (192.168.1.18) has no critical vulnerabilities.
- **Switch 1** (192.168.1.19) has no critical vulnerabilities.
- **Firewall** (192.168.1.22) has no critical vulnerabilities.
- **Access Point** (192.168.1.23) has no critical vulnerabilities.
- **Backup Storage** (192.168.1.26) has no critical vulnerabilities.
- **Server 5** (192.168.1.28) has no critical vulnerabilities.
- **Workstation 4** (192.168.1.29) has no critical vulnerabilities.
- **Server 6** (192.168.1.32) has no critical vulnerabilities.
- **Storage Array** (192.168.1.33) has no critical vulnerabilities.
- **Workstation 5** (192.168.1.37) has no critical vulnerabilities.
- **Server 8** (192.168.1.40) has no critical vulnerabilities.
- **Workstation 6** (192.168.1.41) has no critical vulnerabilities.
- **Printer 3** (192.168.1.44) has no critical vulnerabilities.
- **Router 3** (192.168.1.45) has no critical vulnerabilities.
- **Firewall 2** (192.168.1.49) has no critical vulnerabilities.
- **Access Point 2** (192.168.1.50) has the following vulnerabilities:
  - Session fixation (CVSS Score: 8.6)

## Security Events

- **login_attempts.log:** 2024-01-29 12:02:15 | admin456 | Failure
- **login_attempts.log:** 2024-01-29 12:04:45 | user123 | Failure
- **login_attempts.log:** 2024-01-29 12:07:12 | admin456 | Failure
- **login_attempts.log:** 2024-01-29 12:09:40 | user123 | Failure
- **login_attempts.log:** 2024-01-29 12:12:08 | admin456 | Failure
- **login_attempts.log:** 2024-01-29 12:15:50 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:18:18 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:20:46 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:23:14 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:25:42 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:28:10 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:30:38 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:33:06 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:35:34 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:38:02 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:40:30 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:42:58 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:45:26 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:47:54 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:50:22 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:52:50 | guest789 | Failure
- **login_attempts.log:** 2024-01-29 12:55:18 | john_doe | Failure
- **login_attempts.log:** 2024-01-29 12:57:46 | guest789 | Failure

## Login Attempts


## Intrusion Alerts

