import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

username = "lasya.singamsetty@gmail.com"
password = "YOUR_NEW_APP_PASSWORD"

server.login(username, password)

to = "lasya7.singamsetty@gmail"
subject = "python content"
matter = "use the below file"

msg = MIMEMultipart()
msg["from"] = username
msg["to"] = to
msg["subject"] = subject

msg.attach(MIMEText(matter))

img = r"C:\Users\singa\Downloads\S.A LASYA PRIYA.jpg"

file = open(img, "rb")
attachment = MIMEBase("application", "octet-stream")

attachment.set_payload(file.read())

encoders.encode_base64(attachment)

attachment.add_header("Content-Disposition", f"attachment; filename={img}")

msg.attach(attachment)

print("done")

server.sendmail(username, to, msg.as_string())
print("success")

file.close()
server.quit()
