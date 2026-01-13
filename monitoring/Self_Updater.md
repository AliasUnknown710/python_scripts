# Self_Updater.py

Automatically updates git repositories and restarts scripts.

## Overview

Keeps your automation scripts up-to-date by pulling latest changes from git and optionally restarting dependent scripts.

## Usage

### As a Module

```python
from Self_Updater import update_repo

update_repo("/path/to/automation-scripts")
```

### As a Script

```bash
python3 Self_Updater.py
```

## Configuration

Update the repository path in the script:

```python
if __name__ == "__main__":
    update_repo("/path/to/your/repo")
```

## Function Reference

```python
def update_repo(repo_path: str) -> None:
    """
    Update git repository and restart dependent scripts.
    
    Args:
        repo_path (str): Full path to git repository
    """
```

## How It Works

1. Changes directory to repository
2. Runs `git pull origin main`
3. Outputs update status
4. Optionally restarts scripts

## Examples

### Basic Update
```python
from Self_Updater import update_repo

# Update the repository
update_repo("/home/user/automation-scripts")

# Output: Repo updated. Restarting script...
```

### Update and Restart
```python
from Self_Updater import update_repo
import subprocess

update_repo("/home/user/automation-scripts")

# Restart a specific script after update
subprocess.run(["python3", "main_script.py"])
```

### Scheduled Updates (Cron)

Edit crontab:
```bash
crontab -e
```

Add a scheduled update task:
```bash
# Update every 6 hours
0 */6 * * * python3 /path/to/Self_Updater.py

# Update daily at 3 AM
0 3 * * * python3 /path/to/Self_Updater.py
```

### Scheduled Updates (Windows Task Scheduler)

Create a scheduled task:
```powershell
schtasks /create `
    /tn "UpdateScripts" `
    /tr "python3 C:\path\to\Self_Updater.py" `
    /sc hourly `/mo 6
```

## Common Patterns

### Update and Email Results
```python
from Self_Updater import update_repo
from monitoring.Email_Notifier import send_alert
import subprocess

try:
    update_repo("/path/to/repo")
    send_alert(
        "Scripts Updated",
        "Automation scripts have been updated successfully",
        "admin@example.com"
    )
except Exception as e:
    send_alert(
        "Update Failed",
        f"Failed to update scripts: {str(e)}",
        "admin@example.com"
    )
```

### Update Multiple Repositories
```python
from Self_Updater import update_repo

repos = [
    "/path/to/repo1",
    "/path/to/repo2",
    "/path/to/repo3"
]

for repo in repos:
    try:
        update_repo(repo)
        print(f"✓ Updated {repo}")
    except Exception as e:
        print(f"✗ Failed to update {repo}: {e}")
```

### Update with Version Check
```python
from Self_Updater import update_repo
import subprocess

# Check current version
result = subprocess.run(
    ["git", "rev-parse", "--short", "HEAD"],
    capture_output=True,
    text=True,
    cwd="/path/to/repo"
)
old_version = result.stdout.strip()

# Update
update_repo("/path/to/repo")

# Check new version
result = subprocess.run(
    ["git", "rev-parse", "--short", "HEAD"],
    capture_output=True,
    text=True,
    cwd="/path/to/repo"
)
new_version = result.stdout.strip()

print(f"Updated from {old_version} to {new_version}")
```

## Requirements

- Python 3.7+
- Git installed and configured
- Repository must be a git clone
- Write access to repository directory
- Network access to remote repository

## Troubleshooting

### "fatal: not a git repository"
The specified path is not a git repository.

**Solution:**
```bash
cd /path/to/repo
git init
git remote add origin https://github.com/user/repo.git
```

### "Authentication failed"
Git can't authenticate with remote repository.

**Solutions:**
1. Configure git credentials:
   ```bash
   git config credential.helper store
   git pull  # You'll be prompted for credentials
   ```

2. Use SSH key:
   ```bash
   git remote set-url origin git@github.com:user/repo.git
   ```

3. Use personal access token (GitHub):
   ```bash
   git remote set-url origin https://USERNAME:TOKEN@github.com/user/repo.git
   ```

### "Permission denied"
Script doesn't have write access to repository.

**Solution:**
```bash
# Check ownership
ls -la /path/to/repo

# Change if needed
sudo chown -R user:user /path/to/repo

# Set permissions
chmod -R u+rwx /path/to/repo
```

### Updates Downloaded but Not Merged
Check for merge conflicts:

```bash
cd /path/to/repo
git status
git pull --rebase origin main  # Or git merge FETCH_HEAD
```

## Advanced: Git Configuration

### Set default branch
```bash
cd /path/to/repo
git remote set-head origin main
```

### Use different branch
Modify the script to specify branch:
```python
def update_repo(repo_path: str, branch: str = "main") -> None:
    os.chdir(repo_path)
    subprocess.run(["git", "pull", "origin", branch])
```

### Add retry logic
```python
import subprocess
import time

def update_repo_with_retry(repo_path: str, retries: int = 3) -> None:
    for attempt in range(retries):
        try:
            os.chdir(repo_path)
            subprocess.run(["git", "pull", "origin", "main"], check=True)
            print("✓ Update successful")
            return
        except subprocess.CalledProcessError as e:
            if attempt < retries - 1:
                print(f"⚠ Update failed, retrying... ({attempt + 1}/{retries})")
                time.sleep(5)  # Wait 5 seconds before retry
            else:
                print(f"✗ Update failed after {retries} attempts")
                raise
```

## Integration Examples

### Monitor and Auto-Update
```bash
#!/bin/bash
# Check repository and auto-update if behind

cd /path/to/repo
UPSTREAM=${1:-@{u}}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo "✓ Already up to date"
elif [ $LOCAL = $BASE ]; then
    echo "⚠ Updating..."
    python3 Self_Updater.py
else
    echo "! Local changes, manual update needed"
fi
```

## Security Considerations

⚠️ **Important:**

1. **Protect credentials:**
   - Use SSH keys for authentication
   - Never hardcode passwords
   - Use credential helpers

2. **Verify commits:**
   - Check git signatures
   - Review updates before deploying
   - Use protected branches

3. **Test updates:**
   - Test in dev/staging first
   - Have rollback plan
   - Monitor after updates

## Requirements

- Python 3.7+
- Git installed (`git --version` should work)
- Writable repository directory
- Network access to remote

## Related Tools

- [monitoring/Usage_Tracker.py](Usage_Tracker.py) - Track script executions
- [monitoring/Email_Notifier.py](Email_Notifier.py) - Send update notifications
- [log_analysis/](../log_analysis/README.md) - Monitor update logs

---

**Parent Directory:** [README.md](README.md)
