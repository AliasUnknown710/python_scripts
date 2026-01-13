import re

with open(".env") as f:
    for line in f:
        if re.search(r"(KEY|SECRET|TOKEN|PASSWORD|API|JWT)", line, re.IGNORECASE):
            print(f"[!] Suspicious line: {line.strip()}")
