from email.message import EmailMessage

import ssl
import smtplib

email_sender ="safarayussif@gmail.com"
email_password= "aprv lmjm aoda ckkj"
email_receiver="abdulhaqqamadu123@gmail.com"
subject="Rabeel's email sender"
body=""""
 I created an email sender using python language
"""
em =EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())