# validate_manifest.py

Comprehensive manifest validation with detailed asset reporting.

## Usage

```python
from validate_manifest import load_manifest, validate_assets

manifest = load_manifest("manifest.json")
missing = validate_assets(manifest)

if missing:
    print("[!] Missing assets:")
    for label, path in missing:
        print(f"- {label}: {path}")
else:
    print("[✓] All assets present")
```

## How It Works

1. Loads manifest from manifest.json
2. Validates each asset path exists
3. Returns list of missing assets

## Manifest Format

```json
{
  "logo": "static/img/logo.png",
  "favicon": "static/img/favicon.ico",
  "config": "config/app.yaml"
}
```

## Example Output

```
[!] Missing assets:
- favicon: static/img/favicon.ico
- config: config/app.yaml

[✓] All assets present
```

## Requirements

- Python 3.7+
- manifest.json in working directory
- Read access to asset locations

## Use Cases

- Pre-deployment validation
- Build verification
- Asset inventory checks
- Package completeness validation

---

**Parent Directory:** [README.md](README.md)
