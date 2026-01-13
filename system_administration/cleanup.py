import os, platform, json, shutil
from typing import List, Dict, Any

CONFIG_PATH = "config.json"

def load_config() -> Dict[str, Any]:
    with open(CONFIG_PATH) as f:
        return json.load(f)

def cleanup_paths(paths: List[str]) -> None:
    for path in paths:
        if os.path.exists(path):
            try:
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"[✓] Deleted file: {path}")
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"[✓] Deleted directory: {path}")
            except Exception as e:
                print(f"[!] Failed to delete {path}: {e}")
        else:
            print(f"[-] Not found: {path}")

def main() -> None:
    config = load_config()
    system = platform.system().lower()

    if system not in config:
        print(f"[!] No cleanup config for OS: {system}")
        return

    print(f"[✓] Running cleanup for {system}")
    cleanup_paths(config[system]["paths"])

if __name__ == "__main__":
    main()
