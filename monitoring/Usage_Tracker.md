# Usage_Tracker.py

Logs script execution timestamps for usage tracking and audit trails.

## Overview

Records when scripts are executed with ISO-formatted timestamps. Perfect for creating audit trails, tracking automation effectiveness, and identifying usage patterns.

## Usage

### As a Module

```python
from Usage_Tracker import log_usage

log_usage("script_name.py")
```

### As a Script

```bash
python3 Usage_Tracker.py
```

## Function Reference

```python
def log_usage(script_name: str, log_file: str = "usage.log") -> None:
    """
    Log script execution with timestamp.
    
    Args:
        script_name (str): Name of the script being logged
        log_file (str): Path to log file (default: "usage.log")
    """
```

## Configuration

### Default Behavior
By default, logs to `usage.log` in the current directory.

### Custom Log File
```python
from Usage_Tracker import log_usage

# Log to custom file
log_usage("my_script.py", log_file="/var/log/automation.log")
```

## Examples

### Basic Usage
```python
from Usage_Tracker import log_usage

# Log execution at start of script
log_usage("backup_script.py")

# Rest of script...
print("Running backup...")
```

### In Multiple Scripts

**main_script.py:**
```python
from Usage_Tracker import log_usage
import sys

log_usage(sys.argv[0])  # Logs this script's name
# Do work...
```

**helper_script.py:**
```python
from Usage_Tracker import log_usage
import sys

log_usage(sys.argv[0])  # Logs helper_script.py
# Do work...
```

### Log File Location Strategies

**Option 1: Relative Path (default)**
```python
log_usage("script.py")  # Creates usage.log in current directory
```

**Option 2: Absolute Path**
```python
log_usage("script.py", log_file="/var/log/automation/usage.log")
```

**Option 3: Per-Script Log**
```python
log_usage("backup.py", log_file="/var/log/backup_usage.log")
log_usage("cleanup.py", log_file="/var/log/cleanup_usage.log")
```

## Log Output Format

Each log entry includes:
- **Timestamp**: ISO 8601 format (YYYY-MM-DDTHH:MM:SS.ffffff)
- **Script Name**: Name of executed script

```
2026-01-13T10:30:45.123456 - Ran backup_script.py
2026-01-13T10:31:12.456789 - Ran cleanup_script.py
2026-01-13T10:32:01.789012 - Ran report_generator.py
```

## Analysis Examples

### Count Executions by Script
```bash
awk '{print $NF}' usage.log | sort | uniq -c | sort -rn
```

Output:
```
     45 backup_script.py
     42 cleanup_script.py
     21 report_generator.py
```

### Find Recent Activity
```bash
# Last 10 executions
tail -10 usage.log

# Today's executions
grep "2026-01-13" usage.log
```

### Execution Time Analysis
```bash
# Show execution pattern
grep "backup_script.py" usage.log | head -20
```

### Parse with Python
```python
from datetime import datetime

with open("usage.log") as f:
    for line in f:
        timestamp, _, script = line.strip().partition(" - Ran ")
        dt = datetime.fromisoformat(timestamp)
        print(f"{script}: {dt.strftime('%A %H:%M')}")
```

## Integration Examples

### Automated Logging in All Scripts
Create a base script template:

```python
# script_template.py
from Usage_Tracker import log_usage
import sys
import os

def setup_logging():
    """Setup usage tracking"""
    log_file = os.path.join("/var/log/automation", f"{os.path.basename(__file__)}.log")
    log_usage(sys.argv[0], log_file=log_file)

def main():
    setup_logging()
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

### With Error Logging
```python
from Usage_Tracker import log_usage
import sys
import traceback

log_usage(sys.argv[0])

try:
    # Your code
    pass
except Exception as e:
    # Log error occurrence
    with open("error.log", "a") as f:
        f.write(f"{e}\n{traceback.format_exc()}\n")
    raise
```

### With Performance Tracking
```python
from Usage_Tracker import log_usage
import sys
import time

start = time.time()
log_usage(sys.argv[0])

# Do work...
print("Processing...")

duration = time.time() - start
with open("usage_detailed.log", "a") as f:
    f.write(f"{sys.argv[0]} took {duration:.2f} seconds\n")
```

### Cron Job with Logging
```bash
#!/bin/bash
# Auto-log script execution

SCRIPT_NAME=$1
SCRIPT_PATH=$2

python3 -c "
from Usage_Tracker import log_usage
log_usage('$SCRIPT_NAME')
"

python3 $SCRIPT_PATH
```

## Log Management

### Rotating Logs

Use `logrotate` (Linux):

Create `/etc/logrotate.d/automation`:
```
/var/log/automation/*.log {
    daily
    rotate 7
    compress
    delaycompress
    notifempty
    create 0640 automation automation
    sharedscripts
}
```

### Archiving Old Logs
```bash
#!/bin/bash
# Archive logs older than 30 days

find /var/log/automation -name "*.log" -mtime +30 -exec gzip {} \;
```

### Log Analysis with AWK
```bash
# Execution count by hour
awk '{print substr($1, 1, 13)}' usage.log | sort | uniq -c

# Scripts run at specific time
grep "T10:00" usage.log
```

## Troubleshooting

### Permission Denied
Log file can't be written.

**Solution:**
```bash
# Check permissions
ls -la usage.log

# Make writable
chmod 644 usage.log

# Or change directory
cd /tmp
python3 /path/to/script.py
```

### File Not Created
Script may not have write access to directory.

**Solution:**
```python
import os

log_dir = "/var/log/automation"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_usage("script.py", log_file=f"{log_dir}/usage.log")
```

### Log File Growing Too Large
Implement log rotation or archiving.

**Quick cleanup:**
```bash
# Keep only last 1000 lines
tail -1000 usage.log > usage_temp.log && mv usage_temp.log usage.log
```

## Best Practices

1. **Log at start of script:**
   ```python
   log_usage(sys.argv[0])
   ```

2. **Use consistent log location:**
   ```python
   log_file = "/var/log/automation/usage.log"
   ```

3. **Include context:**
   ```python
   log_usage(f"{sys.argv[0]} (backup)")  # Include operation type
   ```

4. **Manage log rotation:**
   - Implement logrotate
   - Archive old logs regularly
   - Monitor log file size

5. **Parse and analyze:**
   - Review weekly
   - Identify execution patterns
   - Optimize schedule based on data

## Requirements

- Python 3.7+
- Write access to log file location
- Writable directory for log file

## Related Tools

- [monitoring/Self_Updater.py](Self_Updater.py) - Auto-update scripts
- [monitoring/Email_Notifier.py](Email_Notifier.py) - Send execution reports
- [log_analysis/Log_Summarizer.py](../log_analysis/log_summary_report.py) - Analyze logs

---

**Parent Directory:** [README.md](README.md)
