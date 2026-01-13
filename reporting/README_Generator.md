# README_Generator.py

Automatically generates README files from script directories.

## Usage

```python
from README_Generator import generate_readme

generate_readme("path/to/automation-scripts")

# Custom output
generate_readme("path/to/scripts", output="SCRIPTS.md")
```

## Example

```python
generate_readme("src/scripts", "SCRIPT_INVENTORY.md")
```

## Output

Creates markdown file with listing of all scripts (.py, .sh, .ps1 files).

## Requirements

- Python 3.7+
- Valid directory path
- Read access to directory

---

**Parent Directory:** [README.md](README.md)
