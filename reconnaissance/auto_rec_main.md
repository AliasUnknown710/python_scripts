# auto_rec_main.py

Main orchestrator that runs all reconnaissance modules in sequence.

## Usage

```bash
python3 auto_rec_main.py
```

## How It Works

Runs reconnaissance on target in sequence:
1. Subdomain scanning
2. Port scanning  
3. Service fingerprinting

## Example

```python
import modules.subdomain_scan as sub
import modules.port_scan as port
import modules.service_fingerPrint as fp

target = "example.com"
sub.run(target)
port.run(target)
fp.run(target)
```

## Requirements

- Python 3.7+
- Valid domain/host
- Network connectivity

⚠️ **Only run on systems you own or have written permission to test.**

---

**Parent Directory:** [README.md](README.md)
