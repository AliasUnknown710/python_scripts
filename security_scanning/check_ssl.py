import ssl, socket
from datetime import datetime, timezone

host = "yourdomain.com"  # Replace with target domain
port = 443

ctx = ssl.create_default_context()
with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
    s.connect((host, port))
    cert = s.getpeercert()
    if cert is None:
        raise ValueError(f"No certificate found for {host}")
    not_after = cert.get('notAfter', '')
    if isinstance(not_after, (list, tuple)):
        not_after = str(not_after[0])
    expiry = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
    days_left = (expiry - datetime.now(timezone.utc).replace(tzinfo=None)).days

    print(f"[✓] {host} SSL expires in {days_left} days")
    if days_left < 30:
        print(f"[!] Certificate for {host} expires soon!")
