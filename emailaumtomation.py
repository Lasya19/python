import smtplib
#print(help(smtplib))
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

From="singamsetty.lasya@gmail.com"
password="nztk qphi stzd awhz"

server.login(From,password)
To="bunny.1947k@gmail.com"
subject="python email automation"
info="HI bunny this is sending mail usinh python///"

server.sendmail(From,To,info)
print("success")