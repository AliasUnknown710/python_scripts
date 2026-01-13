# HTML_Report.py

Generates HTML reports from scan data and system information.

## Usage

```python
from HTML_Report import generate_report

data = ["Port 22 open", "Memory usage high", "Missing config"]
generate_report(data)  # Creates report.html

# Custom output file
generate_report(data, output="custom_report.html")
```

## Example

```python
sample_data = [
    "Port 22 open",
    "Port 80 open", 
    "Port 443 open"
]
generate_report(sample_data, "port_scan.html")
```

## Output

Creates formatted HTML with unordered list of items.

## Requirements

- Python 3.7+
- Write access to output directory

---

**Parent Directory:** [README.md](README.md)
