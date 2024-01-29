import smtplib
from email.mime.text import MIMEText
import random

subject = "You've been hacked, Change your password"
bodye = "Your new password: {}"
sender = "sw23d001@mandakh.edu.mn"
recipients = ["ganzoo@mandakh.edu.mn"]
password = "freeze1212"

def generated():
    return int(random.randint(10000, 99999))

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

for _ in range(300):
    rando = generated()
    email = bodye.format(random)
    send_email(subject, email, sender, recipients, password)

print()
