from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.gmail.com"
port = 587
username = "231dddd@gmail.com"
password = "caca"
from_email = username
to_list = ["shassan.bese15seecs@seecs.edu.pk","samarhassanphone@gmail.com"]

A = SMTP(host, port)
A.ehlo()
A.starttls()
A.ehlo()
try:
    A.login(username, password)
    A.sendmail(from_email, to_list, "Hello there this is an email message")
except SMTPAuthenticationError:
    print("cannot not login")
except:
    print("Error!!!")

A.quit()