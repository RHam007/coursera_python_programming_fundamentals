import smtplib
from email.mime.text import MIMEText
import imaplib

# Setup for email connection
smtp_server = "smtp.example.com" #replace with real smtp server info
smtp_port = 587
imap_server = "imap.example.com" #replace with real imap server info
imap_port = 993
email_user = "orders@example.com" #replace with real email info
email_password = "Coursera1000!"

def send_confirmation_email(client_email, client_name):
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_user, email_password)
        message = MIMEText(f"Thank you for your order, {client_name}!")
        message['Subject'] = "Order Confirmation"
        message['From'] = email_user
        message['To'] = client_email
        server.send_message(message)
    pass

def check_new_messages(client_email, client_name):
    with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
        mail.login(email_user, email_password)
        mail.select('inbox')
        status, responses = mail.search(None, '(UNSEEN FROM "%s")' % client_email)
    pass

# Example usage
client_email = "john.smith@example.com" # for real usage as a bulk mailer, this would most likely be a dictionary or list of email addresses
client_name = "John Smith"              # and names using a for loop to iterate.
send_confirmation_email(client_email, client_name)
check_new_messages(client_email, client_name)