# priv_escalation_detector.py

Detects privilege escalation events in system logs.

## Overview

Monitors system logs for suspicious privilege escalation attempts, particularly focusing on sudo session events that may indicate unauthorized privilege escalation.

## Usage

```bash
python3 priv_escalation_detector.py
```

## How It Works

1. Reads from `/var/log/syslog`
2. Searches for lines containing both "sudo" and "session opened"
3. Prints matching events to stdout
4. Useful for identifying unexpected privilege escalations

## Configuration

Update the log file path in the script:

```python
with open("/var/log/syslog") as f:
    # Processing logic
```

## Example Output

```
Privilege escalation: Jan 13 10:30:45 server sudo: user : TTY=pts/0 ; PWD=/home/user ; USER=root ; COMMAND=/bin/bash
Privilege escalation: Jan 13 10:35:12 server sudo: admin : TTY=pts/1 ; PWD=/etc ; USER=root ; COMMAND=/bin/nano
```

## Requirements

- Python 3.7+
- Linux/Unix system (uses /var/log/syslog)
- Read access to `/var/log/syslog` (may require sudo)

## Platform Support

- ✓ Linux
- ✓ Unix
- ✗ Windows (uses different log locations)

## Windows Alternative

For Windows systems, check Event Viewer logs:
```powershell
Get-EventLog -LogName Security -InstanceId 4672 | Select-Object TimeGenerated, Message
```

## Security Considerations

⚠️ **Important:**
- This detects successful privilege escalation events
- Monitor regularly for suspicious patterns
- Correlate with other security logs
- Keep audit logs for compliance

## Common Patterns to Watch For

1. **Unexpected sudo usage:**
   - Unusual times of day
   - Non-standard users
   - Uncommon commands

2. **Session patterns:**
   - Multiple rapid escalations
   - Services escalating privileges
   - Root session opens without typical use

## Integration

Use in monitoring/alerting workflows:

```bash
# Monitor for escalations and send alert
python3 priv_escalation_detector.py | mail -s "Privilege Escalation Alert" admin@example.com
```

## Related Tools

- [log_analysis/README.md](README.md) - Other log analysis tools
- [monitoring/Email_Notifier.py](../monitoring/Email_Notifier.py) - Send alerts
- [reporting/Log_Summarizer.py](../reporting/Log_Summarizer.py) - Summarize logs

## Troubleshooting

### Permission Denied Error
Run with elevated privileges:
```bash
sudo python3 priv_escalation_detector.py
```

### No Output
This may indicate:
- No privilege escalation events found (good!)
- Log file doesn't exist
- Check log file path

### Different Log Locations

System varies by distribution:
- Debian/Ubuntu: `/var/log/auth.log` or `/var/log/syslog`
- RHEL/CentOS: `/var/log/audit/audit.log`
- macOS: `/var/log/system.log`

Update path accordingly.
