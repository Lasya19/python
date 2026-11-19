
#smtp --->simple mail transfer protocol
import smtplib
from email.mime.text import MIMEText
#to connect with server:
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
#user -details:
From="singamsetty.lasya@gmail.com"
password="nztk qphi stzd awhz"
#login to server
server.login(From,password)


To=["bunny.1947k@gmail.com","lasya7.singamsetty@gmail.com"]
subject="python email automation"
info="Hiii bunny this is sending mail using python///"
for users in To:
    msg=MIMEText(info)
    msg["from"]=From

    msg["subject"]=subject
    msg["to"]=users
#send to mail
    server.sendmail(From,users,msg.as_string())
    print(f"sent to{users}")
print("success")

server.quit()