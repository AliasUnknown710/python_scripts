import json
import os
from typing import Dict, List, Tuple, Any

def load_manifest(path: str = "manifest.json") -> Dict[str, Any]:
    with open(path) as f:
        return json.load(f)

def validate_assets(manifest: Dict[str, Any]) -> List[Tuple[str, str]]:
    missing: List[Tuple[str, str]] = []
    for label, path in manifest.items():
        if not os.path.exists(path):
            missing.append((label, path))
    return missing

if __name__ == "__main__":
    manifest = load_manifest()
    missing = validate_assets(manifest)

    if missing:
        print("[!] Missing assets:")
        for label, path in missing:
            print(f"- {label}: {path}")
    else:
        print("[✓] All assets present")
