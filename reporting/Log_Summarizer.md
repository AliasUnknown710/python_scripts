# Log_Summarizer.py

Summarizes log files with occurrence counts for each entry type.

## Usage

```python
from Log_Summarizer import summarize_logs

summarize_logs("path/to/logfile.log")
```

## Example

**Input:**
```
apache request GET
apache request POST
nginx request GET
apache error 500
nginx request GET
```

**Output:**
```
apache: 3
nginx: 2
```

## Requirements

- Python 3.7+
- Read access to log file
- Valid log file path

---

**Parent Directory:** [README.md](README.md)
