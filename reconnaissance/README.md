# Reconnaissance

Network reconnaissance tools for discovering subdomains, scanning ports, and fingerprinting services.

## Overview

The reconnaissance module provides automated discovery and enumeration tools for network mapping and service identification.

## Tools

### [auto_rec_main.py](auto_rec_main.py)
Main orchestrator that runs all reconnaissance modules in sequence.

**Usage:**
```bash
python3 auto_rec_main.py
```

**Description:**
- Orchestrates subdomain scanning
- Performs port scanning
- Runs service fingerprinting
- Combines results from all modules

**Example:**
```python
import modules.subdomain_scan as sub
import modules.port_scan as port
import modules.service_fingerPrint as fp

# Run all reconnaissance modules
target = "example.com"
sub.run(target)
port.run(target)
fp.run(target)
```

**Requirements:**
- Python 3.7+
- Target domain/host must be valid

---

## Modules

### [modules/subdomain_scan.py](modules/subdomain_scan.py)
Discovers subdomains for a given domain.

**Usage:**
```python
import modules.subdomain_scan as sub
sub.run("example.com")
```

**Description:**
- Enumerates subdomains
- Useful for finding hidden services
- Helps identify attack surface

**Output:**
```
Scanning subdomains for example.com...
```

**Requirements:**
- Valid domain name
- Network connectivity

---

### [modules/port_scan.py](modules/port_scan.py)
Scans for open ports on a target host.

**Usage:**
```python
import modules.port_scan as port
port.run("192.168.1.1")
```

**Description:**
- Identifies open ports on target
- Maps available services
- Helps discover running services

**Output:**
```
Scanning ports on 192.168.1.1...
```

**Requirements:**
- Valid IP address or hostname
- Network connectivity to target

---

### [modules/service_fingerPrint.py](modules/service_fingerPrint.py)
Identifies services and versions running on open ports.

**Usage:**
```python
import modules.service_fingerPrint as fp
fp.run("192.168.1.1")
```

**Description:**
- Determines service type on open ports
- Attempts to identify service version
- Useful for vulnerability assessment

**Output:**
```
Fingerprinting services on 192.168.1.1...
```

**Requirements:**
- Valid target host
- Network access to target
- Typically run after port scan

---

## Common Tasks

### Running Full Reconnaissance
```bash
python3 auto_rec_main.py
```

This will run all three modules in sequence on the configured target.

### Individual Module Usage
```python
from modules import subdomain_scan, port_scan, service_fingerPrint

target = "yourdomain.com"
subdomain_scan.run(target)
port_scan.run(target)
service_fingerPrint.run(target)
```

### Specifying Different Targets
Modify the target variable in each module call:
```python
subdomain_scan.run("another-domain.com")
port_scan.run("192.168.1.50")
service_fingerPrint.run("192.168.1.50")
```

## Security & Legal Considerations

⚠️ **IMPORTANT**: Network reconnaissance should only be performed on systems you own or have explicit written permission to test.

Unauthorized network scanning may be:
- Illegal in your jurisdiction
- A violation of computer fraud laws
- A breach of terms of service
- Subject to criminal prosecution

Always:
1. Obtain written authorization before scanning
2. Document your testing scope
3. Be aware of applicable laws in your region
4. Use these tools only for authorized security testing

## Requirements

- Python 3.7+
- Network connectivity
- Valid target (domain or IP address)
- Authorization to perform reconnaissance

## Related Tools

- **[Security Scanning](../security_scanning/README.md)** - For SSL checks, port scanning, and banner grabbing
- **[Reporting](../reporting/README.md)** - Generate reports from reconnaissance data

---

**Parent Directory:** [../README.md](../README.md)
