# ssh_brute_parser.py

Analyzes SSH authentication logs to identify brute force attempts.

## Overview

Parses SSH authentication logs to detect failed login attempts, helping identify brute force attacks and suspicious authentication activity.

## Usage

```bash
python3 ssh_brute_parser.py
```

## How It Works

1. Reads from `/var/log/auth.log`
2. Searches for "Failed password" entries
3. Prints all failed SSH login attempts
4. Helps identify attack patterns

## Configuration

Update the log file path in the script:

```python
with open("/var/log/auth.log") as f:
    # Processing logic
```

## Example Output

```
Jan 13 10:15:23 server sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 54321 ssh2
Jan 13 10:15:45 server sshd[1235]: Failed password for root from 192.168.1.100 port 54322 ssh2
Jan 13 10:16:02 server sshd[1236]: Failed password for user from 192.168.1.105 port 54323 ssh2
```

## Requirements

- Python 3.7+
- Linux/Unix system (uses /var/log/auth.log)
- Read access to `/var/log/auth.log` (may require sudo)

## Platform Support

- ✓ Debian/Ubuntu (uses /var/log/auth.log)
- ✓ Linux
- ✓ Unix
- ✗ Windows

## Windows Alternative

For Windows SSH servers:
```powershell
Get-EventLog -LogName Security | Where-Object {$_.InstanceId -eq 4625} | Select-Object TimeGenerated, Message
```

## Analysis Tips

### Count failed attempts by IP:
```bash
python3 ssh_brute_parser.py | grep -oP '\d+\.\d+\.\d+\.\d+' | sort | uniq -c | sort -rn
```

### Check for specific user attacks:
```bash
python3 ssh_brute_parser.py | grep "user@example"
```

### Find attempts from specific IP:
```bash
python3 ssh_brute_parser.py | grep "192.168.1.100"
```

## Security Responses

Common brute force indicators:
1. **Multiple failed attempts from single IP**
   - Block IP with firewall
   - Use fail2ban to auto-block

2. **Attacks on common usernames**
   - root, admin, test, oracle
   - Monitor these accounts closely

3. **Rapid attempt sequences**
   - Indicates automated attack
   - Implement rate limiting

## Protection Measures

1. **SSH Hardening:**
   ```bash
   # Disable root login
   sed -i 's/^PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
   
   # Change default port
   sed -i 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config
   ```

2. **Use fail2ban:**
   ```bash
   sudo apt-get install fail2ban
   ```

3. **SSH Key Authentication:**
   - Disable password authentication
   - Use SSH keys only

4. **Monitor with fail2ban:**
   ```bash
   sudo systemctl enable fail2ban
   sudo systemctl start fail2ban
   ```

## Integration with Monitoring

Monitor and alert on brute force attempts:

```bash
#!/bin/bash
FAILED_ATTEMPTS=$(python3 ssh_brute_parser.py | wc -l)
if [ $FAILED_ATTEMPTS -gt 100 ]; then
    python3 ../monitoring/Email_Notifier.py \
        "SSH Brute Force Alert" \
        "Detected $FAILED_ATTEMPTS failed SSH attempts" \
        "admin@example.com"
fi
```

## Related Tools

- [log_analysis/README.md](README.md) - Other log analysis tools
- [monitoring/Email_Notifier.py](../monitoring/Email_Notifier.py) - Send security alerts
- [reporting/Log_Summarizer.py](../reporting/Log_Summarizer.py) - Summarize attack patterns

## Troubleshooting

### Permission Denied
Run with elevated privileges:
```bash
sudo python3 ssh_brute_parser.py
```

### No Failed Attempts Found
Good news! This means:
- No recent brute force attacks detected
- SSH is well-protected
- Check if SSH is running

### Different Log Paths by Distribution

- **Debian/Ubuntu:** `/var/log/auth.log`
- **RHEL/CentOS:** `/var/log/secure`
- **macOS:** `/var/log/system.log`

Update the file path accordingly.

## Customization

Modify the search pattern to look for other SSH events:

```python
# Failed connections
"Failed"

# Invalid users
"Invalid user"

# Root login attempts
"root from"

# Disconnections
"Disconnected"
```
