import smtplib
from email.mime.text import MIMEText
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
From="singamsetty.lasya@gmail.com"
password="nztk qphi stzd awhz"
server.login(From,password)
to="lasya7.singamsetty@gmail.com"
subject="sending using python"
matter="today we are going to learn how to send file using python through mail"
msg=MIMEText(matter)
msg["from"]=From
msg["to"]=to
msg["subject"]=subject
server.sendmail(From,to,msg.as_string())
print("sent")
server.quit()