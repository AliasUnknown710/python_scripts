from collections import Counter
with open("logfile.log") as f:
    summary = Counter(line.split()[0] for line in f if line.strip())
for key, count in summary.items():
    print(f"{key}: {count}")
