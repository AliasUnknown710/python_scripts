from typing import List, Tuple

def generate_html_report(missing: List[Tuple[str, str]], output: str = "report.html") -> None:
    with open(output, "w") as f:
        f.write("<html><body><h1>Missing Assets</h1><ul>")
        for label, path in missing:
            f.write(f"<li><strong>{label}</strong>: {path}</li>")
        f.write("</ul></body></html>")
    print(f"[✓] Report saved to {output}")

if __name__ == "__main__":
    # Example usage
    sample_missing = [("logo", "static/img/logo.png"), ("config", "config/settings.json")]
    generate_html_report(sample_missing)
