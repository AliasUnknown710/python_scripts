# report_generator.py

Generates HTML reports with asset listings and validation results.

## Usage

```python
from report_generator import generate_html_report

missing = [
    ("logo", "static/img/logo.png"),
    ("config", "config/settings.json")
]
generate_html_report(missing)  # Creates report.html

# Custom output
generate_html_report(missing, "assets_report.html")
```

## Output

Creates HTML report listing assets with labels and paths.

## Requirements

- Python 3.7+
- Write access to output directory

---

**Parent Directory:** [README.md](README.md)
