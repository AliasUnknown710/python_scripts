# Manifest_Validator.py

Validates manifest files and reports missing assets.

## Usage

```python
from Manifest_Validator import validate_manifest

validate_manifest("manifest.json", "assets/")
```

## How It Works

1. Loads JSON manifest file
2. Checks if each asset exists
3. Reports missing assets

## Manifest Format

```json
{
  "logo": "static/img/logo.png",
  "config": "config/settings.json"
}
```

## Example

```python
validate_manifest("manifest.json", ".")
# Output: Missing assets: ['config/settings.json']
# Or: All assets present.
```

## Requirements

- Python 3.7+
- JSON manifest file
- Asset directory path

---

**Parent Directory:** [README.md](README.md)
