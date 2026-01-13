# scan_env_file.py

Scans .env files for sensitive configuration values and patterns.

## Usage

```bash
python3 scan_env_file.py
```

## How It Works

1. Reads .env file
2. Searches for patterns: KEY, SECRET, TOKEN, PASSWORD, API, JWT
3. Reports suspicious lines

## Example Output

```
[!] Suspicious line: DATABASE_PASSWORD=secretpassword123
[!] Suspicious line: API_KEY=abc123def456
[!] Suspicious line: JWT_SECRET=very_secret_token
```

## Use Cases

- Pre-commit hook to prevent secret commits
- Code review automation
- Security scanning pipelines
- Environment validation

## Requirements

- Python 3.7+
- .env file in working directory
- Read access to .env file

⚠️ **Use as git pre-commit hook to prevent secrets in version control**

---

**Parent Directory:** [README.md](README.md)
