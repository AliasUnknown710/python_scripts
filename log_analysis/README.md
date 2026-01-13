# Log Analysis

Tools for parsing and analyzing system logs to detect security events and generate summaries.

## Tools

### [log_summary_report.py](log_summary_report.py)
Generates a summary report of log file entries by counting occurrences of each unique first field.

**Usage:**
```bash
python3 log_summary_report.py
```

**Description:**
- Reads a `logfile.log` file
- Counts occurrences of each unique value in the first field
- Outputs summary with counts

**Configuration:**
- Change the log file path in the script as needed

---

### [priv_escalation_detector.py](priv_escalation_detector.py)
Detects privilege escalation events in system logs.

**Usage:**
```bash
python3 priv_escalation_detector.py
```

**Description:**
- Monitors `/var/log/syslog` for privilege escalation attempts
- Looks for "sudo" and "session opened" events
- Prints matching lines to stdout

**Requirements:**
- Read access to `/var/log/syslog`
- Linux/Unix system

**Configuration:**
- Update the `/var/log/syslog` path for your system

---

### [ssh_brute_parser.py](ssh_brute_parser.py)
Analyzes SSH authentication logs to identify brute force attempts.

**Usage:**
```bash
python3 ssh_brute_parser.py
```

**Description:**
- Parses authentication logs from `/var/log/auth.log`
- Identifies failed password attempts
- Reports suspicious SSH login activity

**Requirements:**
- Read access to `/var/log/auth.log`
- Linux/Unix system

**Configuration:**
- Update the `/var/log/auth.log` path for your system

---

## Common Tasks

### Analyzing a Custom Log File
Modify the filename in any script to point to your log file:
```python
with open("/path/to/your/logfile.log") as f:
    # Process log
```

### Running Multiple Tools
Create a wrapper script to run all analysis tools:
```bash
python3 log_summary_report.py
python3 priv_escalation_detector.py
python3 ssh_brute_parser.py
```

## Security Notes

⚠️ Log files often contain sensitive information. Be careful when:
- Sharing log analysis output
- Redirecting logs to files
- Running these tools on shared systems

## Requirements

- Python 3.7+
- Read access to system log files
- Linux/Unix system (Windows logs use different locations)

---

**Parent Directory:** [../README.md](../README.md)
