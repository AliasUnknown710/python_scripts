# subdomain_scan.py

Discovers subdomains for a given domain.

## Usage

```python
import modules.subdomain_scan as sub

sub.run("example.com")
```

## Example

```python
from modules import subdomain_scan

subdomain_scan.run("mycompany.com")
# Output: Scanning subdomains for mycompany.com...
```

## Requirements

- Python 3.7+
- Valid domain name
- Network connectivity

## Use Cases

- Identify hidden services
- Discover development domains
- Map attack surface

⚠️ **Only scan domains you own or have permission to test.**

---

**Parent Directory:** [../README.md](../README.md)
