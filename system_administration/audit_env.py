import os

SENSITIVE_KEYS = ["KEY", "SECRET", "TOKEN", "PASSWORD", "API", "JWT"]
for key, value in os.environ.items():
    if any(s in key.upper() for s in SENSITIVE_KEYS):
        print(f"[!] {key} = {value[:6]}... (truncated)")
