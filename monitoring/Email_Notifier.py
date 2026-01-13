import smtplib
import os
from email.message import EmailMessage

def send_alert(subject: str, body: str, to_email: str) -> bool:
    """Send an email alert notification."""
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    sender_email = os.getenv("SENDER_EMAIL", "noreply@example.com")
    password = os.getenv("SMTP_PASSWORD", "")
    
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
