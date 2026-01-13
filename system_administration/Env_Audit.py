import os

def audit_env() -> None:
    for key, _ in os.environ.items():
        if "key" in key.lower() or "token" in key.lower() or "secret" in key.lower():
            print(f"Sensitive env var detected: {key}")

if __name__ == "__main__":
    audit_env()
