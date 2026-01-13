# Monitoring

Tools for system monitoring, usage tracking, and automated repository updates.

## Tools

### [Email_Notifier.py](Email_Notifier.py)
Sends email alerts for system events and notifications.

**Usage:**
```bash
python3 Email_Notifier.py
```

**Description:**
- Provides a reusable function to send email alerts
- Configurable SMTP server and credentials
- Supports custom subjects and message bodies

**Environment Variables:**
```
SMTP_SERVER=smtp.gmail.com          # SMTP server address
SENDER_EMAIL=noreply@example.com   # Sender email address
SMTP_PASSWORD=your_password         # SMTP password
```

**Example:**
```python
from Email_Notifier import send_alert

send_alert(
    subject="System Alert",
    body="Something important happened!",
    to_email="admin@example.com"
)
```

**Requirements:**
- Python 3.7+
- SMTP server access
- Email credentials configured

---

### [Self_Updater.py](Self_Updater.py)
Automatically updates git repositories and restarts scripts.

**Usage:**
```bash
python3 Self_Updater.py
```

**Description:**
- Pulls latest changes from git repository
- Updates the automation scripts
- Can optionally restart scripts after update

**Configuration:**
```python
update_repo("/path/to/automation-scripts")
```

**Requirements:**
- Git installed
- Repository must be a git clone
- Write access to repository directory

**Example:**
```python
from Self_Updater import update_repo

update_repo("/path/to/automation-scripts")
# Optionally restart a script:
# subprocess.run(["python3", "some_script.py"])
```

---

### [Usage_Tracker.py](Usage_Tracker.py)
Logs script execution timestamps for usage tracking.

**Usage:**
```bash
python3 Usage_Tracker.py
```

**Description:**
- Records when scripts are executed
- Stores execution logs with ISO format timestamps
- Useful for audit trails and performance monitoring

**Configuration:**
```python
log_usage("script_name.py", log_file="usage.log")
```

**Default Log File:** `usage.log`

**Example:**
```python
from Usage_Tracker import log_usage

# Log script execution
log_usage("my_script.py")

# Use custom log file
log_usage("my_script.py", log_file="custom.log")
```

**Output Format:**
```
2026-01-13T10:30:45.123456 - Ran script_name.py
2026-01-13T10:31:12.456789 - Ran another_script.py
```

---

## Common Tasks

### Setting Up Email Alerts
1. Configure environment variables:
   ```bash
   export SMTP_SERVER=smtp.gmail.com
   export SENDER_EMAIL=your-email@gmail.com
   export SMTP_PASSWORD=your-app-password
   ```

2. Import and use:
   ```python
   from Email_Notifier import send_alert
   send_alert("Alert", "Message body", "recipient@example.com")
   ```

### Automating Repository Updates
Schedule `Self_Updater.py` with cron (Linux/Mac):
```bash
0 */6 * * * python3 /path/to/Self_Updater.py
```

Or Task Scheduler (Windows):
```
schtasks /create /tn "UpdateScripts" /tr "python3 C:\path\to\Self_Updater.py" /sc hourly
```

### Tracking All Script Executions
Call `log_usage()` at the start of each script:
```python
from Usage_Tracker import log_usage
import sys

log_usage(sys.argv[0])
# Rest of script...
```

## Requirements

- Python 3.7+
- For email: SMTP server access and credentials
- For auto-update: Git installed and repository initialized
- For usage tracking: Write access to log file location

## Security Notes

⚠️ When using email alerts:
- Store credentials in environment variables, not in code
- Use app-specific passwords for Gmail
- Avoid logging sensitive data

---

**Parent Directory:** [../README.md](../README.md)
