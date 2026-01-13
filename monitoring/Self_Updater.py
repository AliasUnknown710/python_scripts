import os
import subprocess

def update_repo(repo_path: str) -> None:
    os.chdir(repo_path)
    subprocess.run(["git", "pull", "origin", "main"])
    print("Repo updated. Restarting script...")

if __name__ == "__main__":
    update_repo("/path/to/automation-scripts")
    # Optionally re-run a specific script after update
    # subprocess.run(["python3", "some_script.py"])
