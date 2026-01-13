# log_summary_report.py

Generates a summary report of log file entries by counting occurrences.

## Overview

This utility reads a log file and creates a summary showing how many times each unique entry appears. Perfect for understanding log patterns and identifying frequent events.

## Usage

```bash
python3 log_summary_report.py
```

## How It Works

1. Opens the specified log file
2. Extracts the first field from each line
3. Counts occurrences of each unique value
4. Prints summary with counts

## Configuration

Edit the script to change the log file path:

```python
with open("logfile.log") as f:
    # Processing logic
```

## Example

**Input Log File (logfile.log):**
```
apache 2026-01-13 10:30:45 GET /index.html 200
apache 2026-01-13 10:30:46 GET /style.css 200
nginx 2026-01-13 10:30:47 GET /app.js 304
apache 2026-01-13 10:30:48 POST /api/data 201
nginx 2026-01-13 10:30:49 GET /image.png 200
```

**Output:**
```
apache: 3
nginx: 2
```

## Requirements

- Python 3.7+
- Read access to log file
- Log file exists at specified path

## Common Use Cases

- Analyzing web server logs
- System log summary
- Identifying most common services/events
- Quick log statistics

## Tips

- Use with grep to filter logs first: `grep "error" logfile.log`
- Redirect output to file: `python3 log_summary_report.py > summary.txt`
- Combine with other log analysis tools for deeper insights

## Related Tools

- [log_analysis/README.md](README.md) - More log analysis tools
- [reporting/Log_Summarizer.py](../reporting/Log_Summarizer.py) - Advanced log summarization
