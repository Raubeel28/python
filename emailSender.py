from email.message import EmailMessage
import os
import ssl
import smtplib

email_sender ="safarayussif@gmail.com"
email_password= "aprv lmjm aoda ckkj"
email_receiver="siniorchair@gmail.com"
subject="Rabeel's email sender"
body="""""
Please read the file below
"""
em =EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

with open('research1.pdf','rb') as file:
    file_data=file.read()
    file_name=file.name
    
em.add_attachment(file_data,maintype='application',filename=file_name,subtype='pdf')




context=ssl.create_default_context
try:
     with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_sender,email_password)
        smtp.send_message(em)
except Exception as e:
    print(f"{e}")