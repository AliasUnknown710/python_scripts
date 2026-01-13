import os

def generate_readme(script_dir, output="README.md"):
    with open(output, "w") as f:
        f.write("# Automation Scripts\n\n")
        f.write("## Scripts\n\n")
        for root, _, files in os.walk(script_dir):
            for file in files:
                if file.endswith((".sh", ".ps1", ".py")):
                    path = os.path.join(root, file)
                    f.write(f"- `{path}`\n")
    print(f"README generated at {output}")

if __name__ == "__main__":
    generate_readme("path/to/automation-scripts")
