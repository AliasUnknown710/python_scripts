# port_scan.py

Scans for open ports on a target host.

## Usage

```python
import modules.port_scan as port

port.run("192.168.1.1")
```

## Example

```python
from modules import port_scan

port_scan.run("target.local")
# Output: Scanning ports on target.local...
```

## Requirements

- Python 3.7+
- Valid IP address or hostname
- Network connectivity to target

## Use Cases

- Identify open ports
- Map available services
- Discover running applications

⚠️ **Only scan systems you own or have permission to test.**

---

**Parent Directory:** [../README.md](../README.md)
