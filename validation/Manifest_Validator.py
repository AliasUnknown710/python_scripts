import json
import os
from typing import List

def validate_manifest(manifest_path: str, asset_dir: str) -> None:
    with open(manifest_path) as f:
        manifest = json.load(f)
    missing: List[str] = []
    for asset in manifest.values():
        if not os.path.exists(os.path.join(asset_dir, asset)):
            missing.append(asset)
    if missing:
        print("Missing assets:", missing)
    else:
        print("All assets present.")

if __name__ == "__main__":
    validate_manifest("path/to/manifest.json", "path/to/assets")
