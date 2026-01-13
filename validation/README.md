# Validation

Tools for validating manifest files and verifying asset integrity.

## Tools

### [Manifest_Validator.py](Manifest_Validator.py)
Validates manifest files and reports missing assets.

**Usage:**
```bash
python3 Manifest_Validator.py
```

**Description:**
- Loads JSON manifest files
- Verifies all referenced assets exist
- Reports missing assets
- Useful for deployment validation

**Manifest Format (manifest.json):**
```json
{
  "logo": "static/img/logo.png",
  "config": "config/settings.json",
  "database": "data/schema.sql"
}
```

**Usage Example:**
```python
from Manifest_Validator import validate_manifest

validate_manifest("path/to/manifest.json", "path/to/assets")
```

**Example Output:**
```
Missing assets: ['config/settings.json']
All assets present.
```

**Requirements:**
- Python 3.7+
- JSON manifest file
- Asset directory path

**Use Cases:**
1. Pre-deployment validation
2. Build verification
3. Asset inventory checks
4. Package completeness validation

---

### [validate_manifest.py](validate_manifest.py)
Comprehensive manifest validation with detailed reporting.

**Usage:**
```bash
python3 validate_manifest.py
```

**Description:**
- Loads and validates manifest files
- Detailed asset validation
- Reports missing assets with labels
- Supports flexible manifest structure

**Manifest Format:**
```json
{
  "logo": "static/img/logo.png",
  "favicon": "static/img/favicon.ico",
  "config": "config/app.yaml",
  "database_init": "scripts/init.sql"
}
```

**Usage Example:**
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

**Example Output:**
```
[!] Missing assets:
- favicon: static/img/favicon.ico
- database_init: scripts/init.sql
```

**Output Format:**
Returns list of tuples: `[(label, path), ...]`

**Requirements:**
- Python 3.7+
- manifest.json in working directory (or specify path)
- Read access to asset locations

**Features:**
- Graceful error handling
- Detailed asset reporting
- Human-readable output format
- Integration-friendly return values

---

## Common Tasks

### Pre-Deployment Validation
```bash
# Validate all assets exist before deployment
python3 validate_manifest.py

# If all assets present, proceed with deployment
if [ $? -eq 0 ]; then
    ./deploy.sh
fi
```

### Creating a Manifest File
```json
{
  "application_config": "config/app.yml",
  "database_schema": "db/schema.sql",
  "logo": "assets/logo.png",
  "stylesheet": "assets/style.css",
  "readme": "README.md",
  "license": "LICENSE"
}
```

### Checking Specific Assets
```python
from validate_manifest import load_manifest, validate_assets

manifest = load_manifest("manifest.json")
missing = validate_assets(manifest)

# Check if specific asset is missing
config_missing = any(label == "config" for label, _ in missing)
if config_missing:
    print("Configuration file is missing!")
```

### Integration with Build Process
```bash
#!/bin/bash
# Validate manifest before building
python3 validate_manifest.py
if [ $? -ne 0 ]; then
    echo "Build failed: Missing required assets"
    exit 1
fi

# Proceed with build
npm run build
```

### Generating Reports of Missing Assets
```python
from validate_manifest import load_manifest, validate_assets
from reporting.report_generator import generate_html_report

manifest = load_manifest("manifest.json")
missing = validate_assets(manifest)

if missing:
    generate_html_report(missing, "missing_assets_report.html")
```

## Manifest Best Practices

1. **Organization:**
   - Group related assets
   - Use descriptive labels
   - Keep paths relative to root

2. **Content:**
   ```json
   {
     "config": {
       "app": "config/app.json",
       "database": "config/database.json"
     },
     "assets": {
       "logo": "assets/images/logo.png",
       "styles": "assets/css/main.css"
     }
   }
   ```

3. **Version Control:**
   - Keep manifest.json in version control
   - Don't include secrets in manifest
   - Use .env for sensitive paths

4. **Validation:**
   - Run validation in CI/CD pipeline
   - Validate before building/deploying
   - Check on production as well

## Troubleshooting

### "Missing assets" Error
1. Check manifest.json path is correct
2. Verify asset paths in manifest are correct
3. Ensure files exist on filesystem
4. Check file permissions

### Manifest Not Loading
```python
import json

# Debug manifest loading
try:
    with open("manifest.json") as f:
        manifest = json.load(f)
    print("Manifest loaded successfully")
except FileNotFoundError:
    print("manifest.json not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

### Path Issues
- Use relative paths from project root
- Test paths before adding to manifest
- Avoid hardcoded absolute paths
- Use forward slashes (/) for cross-platform compatibility

## Requirements

- Python 3.7+
- JSON format manifest file
- Valid file paths
- Read access to asset locations

## Integration with Other Tools

- **[Reporting](../reporting/README.md)** - Generate HTML reports of validation results
- **[System Administration](../system_administration/README.md)** - Audit configurations
- **[Log Analysis](../log_analysis/README.md)** - Log validation events

---

**Parent Directory:** [../README.md](../README.md)
