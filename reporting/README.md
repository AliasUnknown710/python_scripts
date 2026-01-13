# Reporting

Tools for generating reports in various formats from collected data and logs.

## Tools

### [HTML_Report.py](HTML_Report.py)
Generates HTML reports from scan data and system information.

**Usage:**
```bash
python3 HTML_Report.py
```

**Description:**
- Creates formatted HTML reports
- Accepts list of data items
- Outputs professional-looking HTML files
- Default output: `report.html`

**Example:**
```python
from HTML_Report import generate_report

data = [
    "Port 22 open",
    "Memory usage high",
    "Missing config key: DB_PASS"
]
generate_report(data)
generate_report(data, output="custom_report.html")
```

**Output:**
Generates HTML file with structured formatting and styling.

**Requirements:**
- Python 3.7+
- Write access to output directory

---

### [Log_Summarizer.py](Log_Summarizer.py)
Summarizes log file contents with occurrence counts.

**Usage:**
```bash
python3 Log_Summarizer.py
```

**Description:**
- Reads log files
- Counts occurrences of each log entry type
- Generates summary statistics
- Useful for log analysis and trend identification

**Example:**
```python
from Log_Summarizer import summarize_logs

summarize_logs("path/to/logfile.log")
```

**Output:**
```
apache: 245
ssh: 89
cron: 156
kernel: 412
```

**Requirements:**
- Python 3.7+
- Read access to log file

---

### [README_Generator.py](README_Generator.py)
Automatically generates README files from script directories.

**Usage:**
```bash
python3 README_Generator.py
```

**Description:**
- Scans directory for scripts (.py, .sh, .ps1)
- Generates README with file listing
- Useful for documentation automation
- Default output: `README.md`

**Example:**
```python
from README_Generator import generate_readme

generate_readme("path/to/automation-scripts")
generate_readme("path/to/scripts", output="SCRIPTS.md")
```

**Output Format:**
```markdown
# Automation Scripts

## Scripts

- `path/to/script1.py`
- `path/to/script2.sh`
- `path/to/script3.ps1`
```

**Requirements:**
- Python 3.7+
- Write access to output location

---

### [report_generator.py](report_generator.py)
Generates comprehensive HTML reports with asset listings and findings.

**Usage:**
```bash
python3 report_generator.py
```

**Description:**
- Creates detailed HTML scan reports
- Lists missing assets
- Formats findings in HTML structure
- Designed for asset/manifest validation results

**Example:**
```python
from report_generator import generate_html_report

missing_assets = [
    ("logo", "static/img/logo.png"),
    ("config", "config/settings.json")
]
generate_html_report(missing_assets)
generate_html_report(missing_assets, output="assets_report.html")
```

**Output:**
```html
<html>
  <body>
    <h1>Missing Assets</h1>
    <ul>
      <li><strong>logo</strong>: static/img/logo.png</li>
      <li><strong>config</strong>: config/settings.json</li>
    </ul>
  </body>
</html>
```

**Requirements:**
- Python 3.7+
- Write access to output directory

---

## Common Tasks

### Generating a Report from Scan Data
```python
from HTML_Report import generate_report

scan_results = [
    "✓ Port 22 SSH open",
    "✓ Port 80 HTTP open",
    "✓ Port 443 HTTPS open"
]
generate_report(scan_results, "scan_report.html")
```

### Creating Project Documentation
```python
from README_Generator import generate_readme

generate_readme("src/scripts", "SCRIPTS.md")
```

### Analyzing Logs
```python
from Log_Summarizer import summarize_logs

summarize_logs("var/log/apache2/access.log")
```

### Creating Asset Reports
```python
from report_generator import generate_html_report

missing = [
    ("Database Config", "config/database.yml"),
    ("API Key File", ".env")
]
generate_html_report(missing, "missing_assets.html")
```

## Common Report Use Cases

1. **Security Scan Results** - Use `HTML_Report.py` to display port scans, service discovery
2. **Log Analysis** - Use `Log_Summarizer.py` for trend analysis and statistics
3. **Project Inventory** - Use `README_Generator.py` to document script repositories
4. **Asset Validation** - Use `report_generator.py` to report missing files or dependencies

## Customization

Each report generator can be customized:
- Modify output path
- Adjust data formatting
- Add custom styling to HTML reports
- Filter data before reporting

## Requirements

- Python 3.7+
- Write access to output directory
- Source data (logs, scan results, etc.)

## Related Tools

- **[Log Analysis](../log_analysis/README.md)** - Parse logs to feed into reports
- **[Validation](../validation/README.md)** - Validate manifests before reporting
- **[Reconnaissance](../reconnaissance/README.md)** - Gather data for reports

---

**Parent Directory:** [../README.md](../README.md)
