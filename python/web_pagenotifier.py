import requests
import hashlib
import smtplib
from email.message import EmailMessage

URL = 'https://example.com'
LAST_HASH_FILE = 'last_hash.txt'
EMAIL_SENDER = 'you@example.com'
EMAIL_RECEIVER = 'target@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PASS = 'yourpassword'

def get_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def send_alert():
    msg = EmailMessage()
    msg.set_content("🔔 Web page has changed!")
    msg['Subject'] = 'Web Monitor Alert'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
        server.login(EMAIL_SENDER, SMTP_PASS)
        server.send_message(msg)

def main():
    response = requests.get(URL)
    current_hash = get_hash(response.text)

    if os.path.exists(LAST_HASH_FILE):
        with open(LAST_HASH_FILE, 'r') as f:
            old_hash = f.read()
        if old_hash != current_hash:
            send_alert()
            with open(LAST_HASH_FILE, 'w') as f:
                f.write(current_hash)
    else:
        with open(LAST_HASH_FILE, 'w') as f:
            f.write(current_hash)

main()
