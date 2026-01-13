# audit_env.py

Scans environment variables for sensitive information exposure.

## Usage

```bash
python3 audit_env.py
```

## How It Works

Searches for environment variables containing key, token, or secret in the name.

## Example Output

```
Sensitive env var detected: DATABASE_KEY
Sensitive env var detected: API_TOKEN
Sensitive env var detected: JWT_SECRET
```

## Requirements

- Python 3.7+
- Environment variables to audit

## Use Cases

- Pre-deployment security checks
- Verify no secrets in environment
- Audit sensitive configurations

---

**Parent Directory:** [README.md](README.md)
