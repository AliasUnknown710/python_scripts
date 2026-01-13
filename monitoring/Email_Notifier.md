# Email_Notifier.py

Sends email alerts for system events and notifications.

## Overview

A reusable email notification utility that sends alerts via SMTP. Perfect for system monitoring, security alerts, and automated notifications.

## Usage

### As a Module

```python
from Email_Notifier import send_alert

send_alert(
    subject="System Alert",
    body="Something important happened!",
    to_email="admin@example.com"
)
```

### As a Script

```bash
python3 Email_Notifier.py
```

## Configuration

Set environment variables before running:

```bash
export SMTP_SERVER=smtp.gmail.com
export SENDER_EMAIL=noreply@example.com
export SMTP_PASSWORD=your_app_password
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `SMTP_SERVER` | smtp.gmail.com | SMTP server address |
| `SENDER_EMAIL` | noreply@example.com | Sender email address |
| `SMTP_PASSWORD` | "" | SMTP authentication password |

## Configuration for Common Providers

### Gmail
```bash
export SMTP_SERVER=smtp.gmail.com
export SENDER_EMAIL=your-email@gmail.com
export SMTP_PASSWORD=your-app-password
```

⚠️ Use [Google App Password](https://support.google.com/accounts/answer/185833), not your regular password

### Office 365
```bash
export SMTP_SERVER=smtp.office365.com
export SENDER_EMAIL=your-email@company.com
export SMTP_PASSWORD=your-password
```

### Custom SMTP Server
```bash
export SMTP_SERVER=mail.company.com
export SENDER_EMAIL=alerts@company.com
export SMTP_PASSWORD=your-password
```

## Function Reference

```python
def send_alert(subject: str, body: str, to_email: str) -> bool:
    """
    Send an email alert notification.
    
    Args:
        subject (str): Email subject line
        body (str): Email message body
        to_email (str): Recipient email address
        
    Returns:
        bool: True if sent successfully, False if failed
    """
```

## Examples

### Basic Alert
```python
from Email_Notifier import send_alert

send_alert(
    subject="Backup Complete",
    body="Daily backup completed successfully at 2:00 AM",
    to_email="admin@example.com"
)
```

### Error Notification
```python
import traceback
from Email_Notifier import send_alert

try:
    # Some process
    problematic_operation()
except Exception as e:
    send_alert(
        subject="Error in Daily Process",
        body=f"Process failed: {str(e)}\n\n{traceback.format_exc()}",
        to_email="admin@example.com"
    )
```

### Security Alert
```python
from Email_Notifier import send_alert

send_alert(
    subject="Security Alert - Suspicious Login",
    body="Unauthorized login attempt detected from 192.168.1.100",
    to_email="security@example.com"
)
```

### Scheduled Monitoring Alert
```bash
#!/bin/bash
# Alert on disk space
USAGE=$(df / | grep / | awk '{print $5}' | cut -d'%' -f1)
if [ $USAGE -gt 80 ]; then
    python3 -c "
from Email_Notifier import send_alert
send_alert('Disk Space Alert', 
    'Disk usage is at ${USAGE}%', 
    'admin@example.com')
"
fi
```

## Return Values

- `True`: Email sent successfully
- `False`: Failed to send email

## Error Handling

The function catches and logs SMTP errors:

```python
try:
    result = send_alert("Subject", "Body", "recipient@example.com")
    if result:
        print("✓ Alert sent")
    else:
        print("✗ Failed to send alert")
except Exception as e:
    print(f"Error: {e}")
```

## Security Best Practices

⚠️ **Important Security Considerations:**

1. **Never hardcode credentials:**
   ```python
   # ✗ DON'T DO THIS
   password = "mypassword"
   
   # ✓ DO THIS
   password = os.getenv("SMTP_PASSWORD")
   ```

2. **Use environment variables:**
   ```bash
   export SMTP_PASSWORD="secure_password"
   python3 script.py
   ```

3. **Use app-specific passwords:**
   - Gmail: Create [App Password](https://support.google.com/accounts/answer/185833)
   - Don't use your regular password

4. **Store secrets safely:**
   - Use `.env` files (add to `.gitignore`)
   - Use secret management systems
   - Never commit to version control

## Troubleshooting

### "Authentication failed"
```
Error sending email: (535, b'5.7.8 Username and password not accepted')
```

**Solutions:**
1. Verify email and password are correct
2. Check SMTP server is correct
3. For Gmail, use App Password (not regular password)
4. Check if 2FA is enabled (requires app password)

### "Connection refused"
```
Error sending email: [Errno 111] Connection refused
```

**Solutions:**
1. Check SMTP server address
2. Verify port number (usually 587 for TLS)
3. Check firewall rules allow outbound SMTP
4. Test connectivity: `telnet smtp.gmail.com 587`

### "Timeout"
```
Error sending email: socket.timeout: timed out
```

**Solutions:**
1. Check network connectivity
2. Increase timeout value
3. Try different SMTP server
4. Check firewall configuration

## Integration Examples

### With Monitoring Tools
```python
# In a monitoring script
from Email_Notifier import send_alert
import subprocess

result = subprocess.run(["python3", "monitor.py"], capture_output=True)
if result.returncode != 0:
    send_alert(
        "Monitoring Failed",
        result.stderr.decode(),
        "ops@example.com"
    )
```

### With Log Analysis
```python
# Alert on specific log events
from Email_Notifier import send_alert

with open("/var/log/auth.log") as f:
    failed = [line for line in f if "Failed password" in line]
    
if len(failed) > 10:
    send_alert(
        "SSH Brute Force Detected",
        f"Found {len(failed)} failed login attempts",
        "security@example.com"
    )
```

## Requirements

- Python 3.7+
- Network connectivity to SMTP server
- Valid email account with SMTP access
- Environment variables configured

## Related Tools

- [monitoring/Usage_Tracker.py](Usage_Tracker.py) - Track script execution
- [monitoring/Self_Updater.py](Self_Updater.py) - Auto-update scripts
- [security_scanning/](../security_scanning/README.md) - Get data for alerts

---

**Parent Directory:** [README.md](README.md)
