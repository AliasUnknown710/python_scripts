# Port_Scan.py

Scans target host for open ports across a configurable range.

## Overview

Efficient port scanner that identifies open ports on target systems using socket connections with configurable timeout values.

## Usage

```bash
python3 Port_Scan.py
```

## Configuration

Edit target and port range:

```python
target_host = "127.0.0.1"
target_ports = range(20, 1025)  # Scan ports 20-1024
```

## Examples

### Basic Port Scan
```python
target_host = "192.168.1.1"
target_ports = range(1, 65536)  # All ports (slow)

# Output:
# Port 22 is open on 192.168.1.1
# Port 80 is open on 192.168.1.1
# Port 443 is open on 192.168.1.1
```

### Common Ports
```python
common_ports = [21, 22, 25, 53, 80, 110, 143, 443, 445, 3306, 5432, 8080]
scan_ports("target.local", common_ports)
```

## Performance Tips

**Scan faster with smaller ranges:**
```python
# Fast: Check common ports
scan_ports(host, [22, 80, 443, 3306, 5432])

# Moderate: Check first 1024
scan_ports(host, range(1, 1025))

# Slow: Check all ports
scan_ports(host, range(1, 65536))
```

**Use threading for large ranges:**
```python
from concurrent.futures import ThreadPoolExecutor

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=1):
            print(f"Port {port} open")
    except:
        pass

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(lambda p: check_port(host, p), range(1, 1025))
```

## Common Port Reference

| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 8080 | HTTP Alt |

## Requirements

- Python 3.7+
- Network connectivity
- Target must be accessible
- Authorization to scan

## Legal Considerations

⚠️ **Only scan systems you own or have written permission to test.**

Unauthorized port scanning is illegal in many jurisdictions.

---

**Parent Directory:** [README.md](README.md)
