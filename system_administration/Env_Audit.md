# Env_Audit.py

Audits environment variables for sensitive configuration exposure.

## Usage

```bash
python3 Env_Audit.py
```

## How It Works

Scans all environment variables for sensitive keywords: key, token, secret.

## Example Output

```
Sensitive env var detected: DB_KEY
Sensitive env var detected: API_TOKEN  
Sensitive env var detected: SECRET_PASS
```

## Requirements

- Python 3.7+
- Environment to audit

## Use Cases

- Security audit before deployment
- Verify environment configuration
- Identify exposed secrets

---

**Parent Directory:** [README.md](README.md)
