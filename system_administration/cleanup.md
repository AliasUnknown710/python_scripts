# cleanup.py

Cross-platform cleanup tool with configuration-based path management.

## Usage

```bash
python3 cleanup.py
```

## Configuration

Create `config.json` with OS-specific cleanup paths:

```json
{
  "windows": {
    "paths": ["C:\\Windows\\Temp", "C:\\temp"]
  },
  "linux": {
    "paths": ["/tmp", "~/.cache"]
  },
  "darwin": {
    "paths": ["/var/tmp", "~/Library/Caches"]
  }
}
```

## Features

- OS detection (Windows, Linux, macOS)
- Deletes files and directories
- Error reporting per item
- Reports missing items

## Output

```
[✓] Running cleanup for linux
[✓] Deleted file: /tmp/file.txt
[✓] Deleted directory: ~/.cache/app
[!] Failed to delete /tmp/protected: Permission denied
[-] Not found: /var/tmp/missing
```

## Requirements

- Python 3.7+
- config.json in same directory
- Appropriate permissions for cleanup paths

---

**Parent Directory:** [README.md](README.md)
