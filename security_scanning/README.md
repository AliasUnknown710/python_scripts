# Security Scanning

Tools for security testing including SSL certificate validation, port scanning, and service enumeration.

## Tools

### [check_ssl.py](check_ssl.py)
Checks SSL/TLS certificate expiration dates and provides warnings.

**Usage:**
```bash
python3 check_ssl.py
```

**Description:**
- Connects to HTTPS servers
- Retrieves SSL certificate information
- Calculates days until expiration
- Issues warnings for certificates expiring within 30 days

**Configuration:**
```python
host = "yourdomain.com"  # Replace with target domain
port = 443              # Standard HTTPS port
```

**Example Output:**
```
[✓] example.com SSL expires in 45 days
[!] domain.com Certificate expires soon! (8 days)
```

**Requirements:**
- Python 3.7+
- Network connectivity to target HTTPS server
- Valid domain name or IP

**Security Notes:**
- Use for websites you administer
- Helpful for monitoring certificate expiration
- Can be scheduled to run periodically

---

### [netcat_banner.py](netcat_banner.py)
Performs service banner grabbing to identify running services.

**Usage:**
```bash
python3 netcat_banner.py
```

**Description:**
- Connects to target ports
- Retrieves service banners
- Identifies service type and version
- Helps map network services

**Configuration:**
```python
host = "192.168.1.100"
ports = [21, 22, 80, 443]
```

**Example Output:**
```
[+] Port 22 banner: SSH-2.0-OpenSSH_7.4
[+] Port 80 banner: HTTP/1.1 200 OK
[-] Port 443 closed or filtered
```

**Requirements:**
- Python 3.7+
- Network connectivity to target
- Ports must be accessible
- May require elevated privileges for lower port numbers

**Legal Considerations:**
- Only scan systems you own or have permission to test
- Unauthorized port scanning may be illegal

---

### [Port_Scan.py](Port_Scan.py)
Scans target host for open ports across a configurable range.

**Usage:**
```bash
python3 Port_Scan.py
```

**Description:**
- Scans port range on target host
- Identifies open ports
- Uses socket connections with timeout
- Efficient scanning with fast feedback

**Configuration:**
```python
target_host = "127.0.0.1"
target_ports = range(20, 1025)  # Scan ports 20-1024
```

**Example Output:**
```
Port 22 is open on 127.0.0.1
Port 80 is open on 127.0.0.1
Port 443 is open on 127.0.0.1
```

**Requirements:**
- Python 3.7+
- Network connectivity to target
- May be slow for large port ranges (can be optimized with threading)

**Performance Tips:**
- Use smaller port ranges for faster results
- Common ports: 22, 80, 443, 3306, 5432, 8080
- Implement threading for large ranges

---

## Common Tasks

### Checking Your Website's SSL Certificate
```python
import check_ssl

check_ssl.host = "mywebsite.com"
# Run the script
```

### Discovering Services on a Server
```bash
# First scan ports
python3 Port_Scan.py

# Then grab banners from open ports
python3 netcat_banner.py
```

### Monitoring Certificate Expiration
Schedule `check_ssl.py` to run daily:
```bash
# Linux/Mac cron
0 8 * * * python3 /path/to/check_ssl.py

# Or use a scheduled task to email results
0 8 * * * python3 /path/to/check_ssl.py | mail -s "SSL Check" admin@example.com
```

### Quick Port Scan
```python
from Port_Scan import scan_ports

# Scan common web ports
scan_ports("192.168.1.1", range(80, 81))
scan_ports("192.168.1.1", range(443, 444))
```

### Service Enumeration
```bash
# 1. Scan ports
python3 Port_Scan.py

# 2. Grab banners from open ports
python3 netcat_banner.py

# 3. Check SSL if HTTPS detected
python3 check_ssl.py
```

## Security & Legal Considerations

⚠️ **CRITICAL**: Port scanning and service enumeration should only be performed on systems you:
- Own
- Operate
- Have explicit written permission to test

**Legal risks include:**
- Computer Fraud and Abuse Act (CFAA) violations in the US
- Similar laws in other jurisdictions
- Civil liability
- Criminal prosecution

**Always:**
1. Obtain written authorization
2. Scope testing appropriately
3. Document your activities
4. Be aware of local laws
5. Use only on test/authorized systems

## Optimization Tips

### Threading for Faster Scans
Consider implementing threading for large port ranges:
```python
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    # Scanning logic here
    pass

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(lambda p: scan_port(host, p), ports)
```

### Timeout Configuration
Adjust timeout for reliability vs speed:
```python
# Faster but may miss some ports
socket.create_connection((host, port), timeout=1)

# More reliable but slower
socket.create_connection((host, port), timeout=3)
```

## Requirements

- Python 3.7+
- Network connectivity to target systems
- Socket library (built-in)
- SSL library (built-in) for check_ssl.py
- Authorization to perform security testing

## Related Tools

- **[Reconnaissance](../reconnaissance/README.md)** - Network discovery and enumeration
- **[Reporting](../reporting/README.md)** - Generate reports from scan results
- **[Log Analysis](../log_analysis/README.md)** - Analyze security logs

---

**Parent Directory:** [../README.md](../README.md)
