# service_fingerPrint.py

Identifies services and versions running on open ports.

## Usage

```python
import modules.service_fingerPrint as fp

fp.run("192.168.1.1")
```

## Example

```python
from modules import service_fingerPrint

service_fingerPrint.run("target.local")
# Output: Fingerprinting services on target.local...
```

## Requirements

- Python 3.7+
- Valid target host
- Network access to target
- Typically run after port_scan

## Use Cases

- Identify service types and versions
- Vulnerability assessment
- Service discovery

⚠️ **Only scan systems you own or have permission to test.**

---

**Parent Directory:** [../README.md](../README.md)
