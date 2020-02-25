import requests
import smtplib
import os

email= "singhamit.76683@gmail.com"
password = "hmpcwabmeofmmafq"

r = requests.get("https://support.google.com/accounts/answer/185839", timeout=5)
print(r.status_code)
if r.status_code != 300:
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email,password)
        subject ='YOUR SITE IS DOWN'
        body = "server restart nedded"
        msg = f'subject: {subject}\n\n{body}'
        smtp.sendmail(email,email,msg)
