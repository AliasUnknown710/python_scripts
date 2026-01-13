import socket
from typing import Union, List

def scan_ports(host: str, ports: Union[List[int], range]) -> None:
    for port in ports:
        try:
            with socket.create_connection((host, port), timeout=1):
                print(f"Port {port} is open on {host}")
        except:
            pass

if __name__ == "__main__":
    target_host = "127.0.0.1"
    target_ports = range(20, 1025)
    scan_ports(target_host, target_ports)
