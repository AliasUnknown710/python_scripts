import socket

host = "192.168.1.100"
ports = [21, 22, 80, 443]

for port in ports:
    try:
        with socket.create_connection((host, port), timeout=3) as s:
            banner = s.recv(1024).decode(errors="ignore")
            print(f"[+] Port {port} banner: {banner.strip()}")
    except:
        print(f"[-] Port {port} closed or filtered")
