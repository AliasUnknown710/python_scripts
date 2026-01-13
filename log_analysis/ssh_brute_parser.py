with open("/var/log/auth.log") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())
