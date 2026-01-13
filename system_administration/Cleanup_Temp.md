# Cleanup_Temp.py

Removes temporary files from specified directory.

## Usage

```bash
python3 Cleanup_Temp.py
```

## Configuration

Edit the temporary directory path:

```python
TEMP_DIR = "/home/username/temp"
```

## How It Works

1. Lists files in TEMP_DIR
2. Deletes each file
3. Reports success or errors

## Example Output

```
[✓] Deleted: file1.tmp
[✓] Deleted: file2.log
[!] Error deleting file3.tmp: Permission denied
```

## Requirements

- Python 3.7+
- Write access to cleanup directory
- Valid directory path

## Caution

⚠️ **Permanently deletes files** - test on small directory first.

---

**Parent Directory:** [README.md](README.md)
