# netcat_banner.py

Performs service banner grabbing to identify running services and their versions.

## Overview

Connects to target ports and retrieves service banners, helping identify service types, versions, and configurations for security assessment and network mapping.

## Usage

```bash
python3 netcat_banner.py
```

## Configuration

Edit the target host and ports to scan:

```python
host = "192.168.1.100"
ports = [21, 22, 80, 443, 3306, 5432, 8080]
```

## How It Works

1. Iterates through specified ports
2. Creates socket connection to each port
3. Receives initial service banner
4. Reports open ports and service information
5. Gracefully handles closed/filtered ports

## Examples

### Basic Usage
```python
host = "192.168.1.100"
ports = [21, 22, 80, 443]

# Output:
# [+] Port 22 banner: SSH-2.0-OpenSSH_7.4
# [+] Port 80 banner: HTTP/1.1 200 OK...
# [-] Port 21 closed or filtered
# [-] Port 443 closed or filtered
```

### Scan Web Servers
```python
host = "webserver.example.com"
ports = [80, 443, 8080, 8443, 8000]

# Identifies web server type and version
```

### Scan Database Servers
```python
host = "db.internal.local"
ports = [3306, 5432, 1433, 27017, 6379]

# Identifies database services:
# MySQL, PostgreSQL, MSSQL, MongoDB, Redis
```

### Scan Common Services
```python
host = "target.local"
common_ports = [
    21,     # FTP
    22,     # SSH
    25,     # SMTP
    53,     # DNS
    80,     # HTTP
    110,    # POP3
    143,    # IMAP
    443,    # HTTPS
    445,    # SMB
    3306,   # MySQL
    5432,   # PostgreSQL
    8080,   # HTTP Alt
]
```

## Example Output

```
[+] Port 22 banner: SSH-2.0-OpenSSH_7.4
[+] Port 80 banner: HTTP/1.1 200 OK Server: Apache/2.4.6
[+] Port 443 banner: HTTP/1.1 200 OK Server: nginx/1.14.0
[-] Port 21 closed or filtered
[-] Port 3306 closed or filtered
```

## Use Cases

1. **Network Reconnaissance:**
   - Map running services
   - Identify service versions
   - Detect misconfigurations

2. **Security Audits:**
   - Find exposed services
   - Check for outdated versions
   - Verify service hardening

3. **Vulnerability Assessment:**
   - Identify vulnerable service versions
   - Map attack surface
   - Prioritize patching

## Service Identification

### Common Banners

**SSH:**
```
SSH-2.0-OpenSSH_7.4
SSH-2.0-OpenSSH_8.0
SSH-1.99-OpenSSH_3.9p1
```

**HTTP:**
```
HTTP/1.1 200 OK
Server: Apache/2.4.41
Server: nginx/1.18.0
Server: Microsoft-IIS/10.0
```

**FTP:**
```
220 ProFTPD Server
220 Microsoft FTP Service
220 vsftpd (Very Secure FTP Daemon)
```

**SMTP:**
```
220 mail.example.com ESMTP Postfix
220 mail.example.com Sendmail
```

## Advanced Scanning

### Multi-Host Scanning
```python
hosts = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]
ports = [22, 80, 443, 3306]

for host in hosts:
    print(f"\nScanning {host}:")
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=3) as s:
                banner = s.recv(1024).decode(errors="ignore")
                print(f"[+] {host}:{port} - {banner.strip()[:50]}")
        except:
            print(f"[-] {host}:{port} closed or filtered")
```

### With Threading for Speed
```python
from concurrent.futures import ThreadPoolExecutor
import socket

def scan_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3) as s:
            banner = s.recv(1024).decode(errors="ignore")
            return f"[+] {port}: {banner.strip()[:50]}"
    except:
        return f"[-] {port} closed"

host = "target.local"
ports = range(1, 1025)

with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(lambda p: scan_port(host, p), ports)
    for result in results:
        print(result)
```

### Save Results to File
```python
results = []

for port in ports:
    try:
        with socket.create_connection((host, port), timeout=3) as s:
            banner = s.recv(1024).decode(errors="ignore")
            results.append({
                'port': port,
                'status': 'open',
                'banner': banner.strip()
            })
    except:
        results.append({
            'port': port,
            'status': 'closed',
            'banner': None
        })

import json
with open(f"{host}_scan.json", "w") as f:
    json.dump(results, f, indent=2)
```

## Filtering Output

### Find Specific Service
```bash
python3 netcat_banner.py | grep -i "ssh"
# Or in script:
# Output will show SSH services
```

### Extract Version Numbers
```bash
python3 netcat_banner.py | grep -oP '\d+\.\d+\.\d+'
```

### Count Open Ports
```bash
python3 netcat_banner.py | grep "^\[+\]" | wc -l
```

## Timeout Configuration

Adjust timeout for different network conditions:

```python
# Fast but may miss slow services (1 second)
socket.create_connection((host, port), timeout=1)

# Balanced (3 seconds)
socket.create_connection((host, port), timeout=3)

# Thorough but slower (5 seconds)
socket.create_connection((host, port), timeout=5)
```

## Error Handling

### Handle Different Exceptions
```python
import socket
import errno

for port in ports:
    try:
        with socket.create_connection((host, port), timeout=3) as s:
            banner = s.recv(1024).decode(errors="ignore")
            print(f"[+] Port {port}: {banner.strip()}")
    except socket.timeout:
        print(f"[-] Port {port} timeout (service slow)")
    except socket.refused:
        print(f"[-] Port {port} refused")
    except socket.gaierror:
        print(f"[-] Host {host} not found")
    except Exception as e:
        print(f"[-] Port {port} error: {e}")
```

## Troubleshooting

### "Connection refused"
Normal - port is closed or no service listening.

### "Timeout" 
Service is slow or firewall is filtering.

**Solution:**
- Increase timeout value
- Check if service is running
- Verify firewall rules

### "Invalid host"
Host doesn't exist or DNS issues.

**Solutions:**
```bash
ping 192.168.1.100
nslookup example.com
```

### Decoding Errors
Some services send non-UTF8 data.

**Solution:**
Script already handles with `errors="ignore"` but you can improve:

```python
try:
    banner = s.recv(1024).decode('utf-8', errors='ignore')
except:
    banner = s.recv(1024).decode('latin-1', errors='ignore')
```

## Legal Considerations

⚠️ **CRITICAL:**

**Only scan systems you own or have explicit written permission to scan.**

Banner grabbing is reconnaissance activity that may:
- Be illegal without authorization
- Violate computer fraud laws
- Trigger security alerts
- Be considered an attack attempt

Always:
1. Get written permission
2. Understand applicable laws
3. Document your scope
4. Use on authorized systems only

## Requirements

- Python 3.7+
- Network connectivity to targets
- Socket library (built-in)
- Valid IP addresses or hostnames
- Authorization to scan

## Performance Optimization

For scanning large port ranges, use threading:

```python
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

results = []
lock = Lock()

def scan_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=2) as s:
            banner = s.recv(1024).decode(errors="ignore")
            with lock:
                results.append((port, banner.strip()[:50]))
    except:
        pass

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(lambda p: scan_port(host, p), range(1, 10001))

for port, banner in sorted(results):
    print(f"[+] {port}: {banner}")
```

## Related Tools

- [security_scanning/Port_Scan.py](Port_Scan.py) - Port scanning
- [security_scanning/check_ssl.py](check_ssl.py) - SSL certificate checking
- [reconnaissance/](../reconnaissance/README.md) - Network reconnaissance

---

**Parent Directory:** [README.md](README.md)
