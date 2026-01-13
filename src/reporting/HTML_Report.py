from typing import List

def generate_report(data: List[str], output: str = "report.html") -> None:
    with open(output, "w") as f:
        f.write("<html><body><h1>Scan Report</h1><ul>")
        for item in data:
            f.write(f"<li>{item}</li>")
        f.write("</ul></body></html>")
    print(f"Report saved to {output}")

if __name__ == "__main__":
    sample_data = ["Port 22 open", "Memory usage high", "Missing config key: DB_PASS"]
    generate_report(sample_data)
