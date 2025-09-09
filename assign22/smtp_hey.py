import smtplib
from email.mime.text import MIMEText

def smtp_demo():
    sender = "shakibjamila4101@gmail.com"
    receiver = "akhtarshakib4104@gmail.com"
    password = "czty qiym jqdf lwjc"  # Use Gmail app password, not your login password

    msg = MIMEText("This is a test email from Python (CN Lab Assignment 2).")
    msg["Subject"] = "Test Email"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print("SMTP failed:", e)

smtp_demo()
