from collections import Counter

def summarize_logs(log_path: str) -> None:
    with open(log_path) as f:
        lines = f.readlines()
    summary = Counter(line.split()[0] for line in lines if line.strip())
    for key, count in summary.items():
        print(f"{key}: {count}")

if __name__ == "__main__":
    summarize_logs("path/to/logfile.log")
