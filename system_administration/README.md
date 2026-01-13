# System Administration

Tools for system auditing, cleanup, and environment variable management.

## Tools

### [audit_env.py](audit_env.py)
Scans environment variables for sensitive information.

**Usage:**
```bash
python3 audit_env.py
```

**Description:**
- Detects sensitive environment variables
- Identifies keys, secrets, tokens, passwords
- Helps prevent accidental exposure
- Useful for security audits

**Sensitive Keywords Detected:**
- KEY
- SECRET
- TOKEN
- PASSWORD
- API
- JWT

**Example Output:**
```
[!] DATABASE_KEY = abc123... (truncated)
[!] API_SECRET = xyz789... (truncated)
[!] JWT_TOKEN = token... (truncated)
```

**Requirements:**
- Python 3.7+
- Environment variables to audit

**Security Notes:**
- Only run on systems you control
- Output shows truncated values for security
- Use to audit before deploying to production

---

### [Cleanup_Temp.py](Cleanup_Temp.py)
Removes temporary files from a specified directory.

**Usage:**
```bash
python3 Cleanup_Temp.py
```

**Description:**
- Deletes files in temporary directory
- Helps manage disk space
- Simple file-based cleanup
- Errors are caught and reported

**Configuration:**
```python
TEMP_DIR = "/home/username/temp"
```

**Example Output:**
```
[✓] Deleted: file1.tmp
[✓] Deleted: file2.log
[!] Error deleting file3.tmp: Permission denied
```

**Requirements:**
- Python 3.7+
- Write access to cleanup directory
- Valid directory path

**Caution:**
- Permanently deletes files
- Test on sample directory first
- Back up important data before running

---

### [cleanup.py](cleanup.py)
Cross-platform cleanup tool with configuration-based path management.

**Usage:**
```bash
python3 cleanup.py
```

**Description:**
- Supports Windows, Linux, macOS
- Configuration-driven cleanup paths
- Deletes files and directories
- Provides feedback on each operation

**Configuration File (config.json):**
```json
{
  "windows": {
    "paths": [
      "C:\\Windows\\Temp\\*",
      "C:\\Users\\%username%\\AppData\\Local\\Temp\\*"
    ]
  },
  "linux": {
    "paths": [
      "/tmp/*",
      "~/.cache/*"
    ]
  },
  "darwin": {
    "paths": [
      "/var/tmp/*",
      "~/Library/Caches/*"
    ]
  }
}
```

**Example Output:**
```
[✓] Running cleanup for linux
[✓] Deleted file: /tmp/tempfile.txt
[✓] Deleted directory: ~/.cache/old_data
[!] Failed to delete /tmp/protected: Permission denied
[-] Not found: /tmp/nonexistent
```

**Requirements:**
- Python 3.7+
- config.json in same directory
- Appropriate permissions for cleanup paths

**Features:**
- OS detection (Windows, Linux, macOS)
- File and directory support
- Error handling with feedback
- Paths not found are reported but don't fail

---

### [Env_Audit.py](Env_Audit.py)
Detailed audit of environment variables for security exposure.

**Usage:**
```bash
python3 Env_Audit.py
```

**Description:**
- Scans all environment variables
- Identifies sensitive variable names
- Reports potential security issues
- Similar to audit_env.py with different keywords

**Detection Keywords:**
- key
- token
- secret

**Example Output:**
```
Sensitive env var detected: DB_KEY
Sensitive env var detected: API_TOKEN
Sensitive env var detected: SECRET_PASS
```

**Requirements:**
- Python 3.7+
- Environment to audit

---

### [scan_env_file.py](scan_env_file.py)
Scans .env files for sensitive configuration values.

**Usage:**
```bash
python3 scan_env_file.py
```

**Description:**
- Reads .env configuration files
- Identifies sensitive patterns
- Reports suspicious lines
- Helps prevent secrets in version control

**Patterns Detected:**
- KEY
- SECRET
- TOKEN
- PASSWORD
- API
- JWT

**Example Output:**
```
[!] Suspicious line: DATABASE_PASSWORD=secretpassword123
[!] Suspicious line: API_KEY=abc123def456
[!] Suspicious line: JWT_SECRET=very_secret_token
```

**Requirements:**
- Python 3.7+
- .env file in working directory
- Read access to .env file

**Use Cases:**
1. Pre-commit hook to prevent secrets in .env
2. Code review automation
3. Security scanning pipelines
4. Environment variable validation

---

## Common Tasks

### Auditing System Before Deployment
```bash
# Check for exposed environment variables
python3 audit_env.py
python3 Env_Audit.py

# Check .env file for secrets
python3 scan_env_file.py

# Then proceed with deployment
```

### Cleaning Temporary Files
```bash
# Clean specific directory
python3 Cleanup_Temp.py

# Cross-platform cleanup
python3 cleanup.py
```

### Setting Up Automated Cleanup
Schedule with cron (Linux/Mac):
```bash
# Run cleanup daily at 2 AM
0 2 * * * python3 /path/to/cleanup.py

# Run audit weekly
0 3 * * 0 python3 /path/to/audit_env.py
```

### Pre-Commit Hook for Secret Detection
```bash
#!/bin/bash
python3 scan_env_file.py
if [ $? -ne 0 ]; then
    echo "Sensitive data detected in .env file"
    exit 1
fi
```

## Security Best Practices

⚠️ **Environment & Configuration Security:**

1. **Never commit secrets:**
   - Use .env files (add to .gitignore)
   - Use environment variables
   - Use secret management systems

2. **Audit regularly:**
   - Run before deployments
   - Use as pre-commit hooks
   - Schedule periodic audits

3. **Cleanup safely:**
   - Test on non-production first
   - Back up before bulk deletion
   - Monitor disk space

4. **Monitoring:**
   - Set up alerts for suspicious env vars
   - Log audit results
   - Review cleanup logs

## Configuration

### cleanup.py Configuration
Create `config.json` in the same directory:
```json
{
  "windows": {
    "paths": ["C:\\temp", "C:\\Windows\\Temp"]
  },
  "linux": {
    "paths": ["/tmp", "/var/tmp", "~/.cache"]
  }
}
```

## Requirements

- Python 3.7+
- Appropriate file system permissions
- config.json for cleanup.py
- .env file for scan_env_file.py

## Related Tools

- **[Validation](../validation/README.md)** - Validate configuration files
- **[Log Analysis](../log_analysis/README.md)** - Audit log files
- **[Monitoring](../monitoring/README.md)** - Monitor system health

---

**Parent Directory:** [../README.md](../README.md)
