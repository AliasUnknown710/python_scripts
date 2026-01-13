# check_ssl.py

Checks SSL/TLS certificate expiration and provides alerts for soon-to-expire certificates.

## Overview

Connects to HTTPS servers, retrieves SSL certificate information, and alerts when certificates are expiring soon (within 30 days).

## Usage

```bash
python3 check_ssl.py
```

## Configuration

Edit the target domain and port:

```python
host = "yourdomain.com"  # Replace with your domain
port = 443              # Standard HTTPS port
```

## How It Works

1. Creates SSL connection to target host
2. Retrieves certificate information
3. Extracts expiration date
4. Calculates days until expiration
5. Issues warning if < 30 days remaining

## Examples

### Check Your Website
```python
host = "mywebsite.com"
port = 443

# Script will output:
# [✓] mywebsite.com SSL expires in 45 days
# OR
# [!] mywebsite.com Certificate expires soon! (8 days)
```

### Check Multiple Domains

Create a wrapper script:

```bash
#!/bin/bash
# check_multiple_ssl.sh

DOMAINS=("example.com" "api.example.com" "admin.example.com")

for domain in "${DOMAINS[@]}"; do
    python3 -c "
import ssl, socket
from datetime import datetime, timezone

host = '$domain'
port = 443

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
    try:
        s.connect((host, port))
        cert = s.getpeercert()
        if cert is None:
            print(f'✗ No certificate found for {host}')
        else:
            not_after = cert.get('notAfter', '')
            if isinstance(not_after, (list, tuple)):
                not_after = str(not_after[0])
            expiry = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
            days_left = (expiry - datetime.now(timezone.utc).replace(tzinfo=None)).days
            
            if days_left < 30:
                print(f'[!] {host} expires in {days_left} days')
            else:
                print(f'[✓] {host} SSL expires in {days_left} days')
    except Exception as e:
        print(f'✗ Error checking {host}: {e}')
"
done
```

## Example Output

```
[✓] example.com SSL expires in 45 days
[✓] api.example.com SSL expires in 120 days
[!] test.example.com Certificate expires soon! (8 days)
✗ No certificate found for invalid.example.com
```

## Use Cases

1. **Certificate Monitoring:**
   - Schedule daily checks
   - Get alerts before expiration
   - Prevent service outages

2. **Compliance Audits:**
   - Verify all certificates valid
   - Check expiration dates
   - Generate reports

3. **Automated Renewal:**
   - Alert before renewal needed
   - Integrate with Let's Encrypt
   - Track certificate lifecycle

## Scheduling

### Linux/macOS (Cron)

Edit crontab:
```bash
crontab -e
```

Add daily check at 8 AM:
```bash
0 8 * * * python3 /path/to/check_ssl.py
```

### Send Email Report
```bash
0 8 * * * python3 /path/to/check_ssl.py | mail -s "SSL Certificate Check" admin@example.com
```

### With Alerting
```bash
#!/bin/bash
# check_ssl_alert.sh

OUTPUT=$(python3 /path/to/check_ssl.py)

if echo "$OUTPUT" | grep -q "\[!\]"; then
    python3 -c "
from monitoring.Email_Notifier import send_alert
send_alert('SSL Certificate Alert', '$OUTPUT', 'admin@example.com')
"
fi
```

### Windows Task Scheduler

Create a scheduled task:
```powershell
$taskAction = New-ScheduledTaskAction -Execute "python3" -Argument "C:\path\to\check_ssl.py"
$taskTrigger = New-ScheduledTaskTrigger -Daily -At 08:00
$taskSettings = New-ScheduledTaskSettingsSet -StartWhenAvailable
Register-ScheduledTask -TaskName "Check SSL Certificates" -Action $taskAction -Trigger $taskTrigger -Settings $taskSettings
```

## Common Scenarios

### Certificate Renewal Reminder
```bash
#!/bin/bash
# Send reminder to renew certificate 30 days before expiration

python3 check_ssl.py | grep "\[!\]" | while read line; do
    python3 -c "
from monitoring.Email_Notifier import send_alert
send_alert(
    'Certificate Renewal Reminder',
    '$line\n\nPlease renew this certificate soon.',
    'devops@example.com'
)
"
done
```

### Bulk Checking Script

```python
import ssl
import socket
from datetime import datetime, timezone

domains = [
    "example.com",
    "api.example.com",
    "admin.example.com"
]

expired = []
expiring_soon = []
valid = []

for domain in domains:
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
            not_after = cert.get('notAfter', '')
            
            expiry = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
            days_left = (expiry - datetime.now(timezone.utc).replace(tzinfo=None)).days
            
            if days_left < 0:
                expired.append(domain)
            elif days_left < 30:
                expiring_soon.append((domain, days_left))
            else:
                valid.append(domain)
    except Exception as e:
        print(f"Error checking {domain}: {e}")

print(f"Valid: {len(valid)}, Expiring Soon: {len(expiring_soon)}, Expired: {len(expired)}")
```

## Troubleshooting

### "No certificate found"
The connection succeeded but no SSL certificate present.

**Causes:**
- Non-HTTPS service
- Server misconfiguration

**Solution:**
- Verify domain is HTTPS-enabled
- Check if using custom port

### "Connection refused"
Can't reach the server.

**Causes:**
- Host offline
- Port wrong
- Firewall blocking

**Solutions:**
```bash
# Test connectivity
ping yourdomain.com
curl -I https://yourdomain.com

# Try different port
python3 -c "... port = 8443"
```

### "Name resolution failed"
Domain doesn't resolve.

**Causes:**
- Typo in domain name
- DNS issues
- Domain expired

**Solution:**
```bash
nslookup yourdomain.com
```

### "Certificate validation failed"
SSL certificate validation error.

**Causes:**
- Self-signed certificate
- Expired certificate
- Wrong domain

**Solutions:**
1. Create context that doesn't validate:
   ```python
   ctx = ssl.create_default_context()
   ctx.check_hostname = False
   ctx.verify_mode = ssl.CERT_NONE
   ```

2. Or add custom CA:
   ```python
   ctx.load_verify_locations('path/to/ca.pem')
   ```

## Requirements

- Python 3.7+
- Network connectivity to target hosts
- SSL/TLS support
- Valid domain names or IPs

## Security Considerations

⚠️ **Important:**

1. **Only check domains you own or have permission to test**
2. **Don't disable certificate validation in production:**
   ```python
   # ✗ Security risk
   ctx.check_hostname = False
   ctx.verify_mode = ssl.CERT_NONE
   
   # ✓ Safer for testing only
   ```

3. **Secure your monitoring system:**
   - Use HTTPS for reports
   - Restrict access to logs
   - Authenticate checkers

## Performance Tips

For checking many domains, use threading:

```python
from concurrent.futures import ThreadPoolExecutor

def check_domain(domain):
    # Check logic here
    pass

domains = ["example.com", "api.example.com", ...]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(check_domain, domains))
```

## Related Tools

- [security_scanning/Port_Scan.py](Port_Scan.py) - Scan for open ports
- [security_scanning/netcat_banner.py](netcat_banner.py) - Grab service banners
- [monitoring/Email_Notifier.py](../monitoring/Email_Notifier.py) - Send alerts

---

**Parent Directory:** [README.md](README.md)
