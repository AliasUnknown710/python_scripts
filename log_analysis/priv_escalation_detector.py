with open("/var/log/syslog") as f:
    for line in f:
        if "sudo" in line and "session opened" in line:
            print("Privilege escalation:", line.strip())
