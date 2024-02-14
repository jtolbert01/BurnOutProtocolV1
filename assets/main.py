import smtplib

from email.message import EmailMessage

def ask_for_help(event):
  email_address = "email"
  email_password = "pass"
  msg = EmailMessage()
  msg['Subject'] = "BURNOUT NOTICE"
  msg['From'] = email_address
  msg['To'] = "to-address@gmail.com"
  msg.set_content("You need to cheer up Hazel")
  
  print("Asking now")
