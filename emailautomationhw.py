import random
import smtplib
from email.mime.text import MIMEText
class Bank:
    Bank_name="codegnan"
    accounts={}

    def Create_Act(self,act_no,pin,Balance):
        self.act_no=act_no
        self.pin=pin
        self.Balance=Balance

        self.accounts[self.act_no]=[self.pin,self.Balance]
        print("account created succefully")

    def Login(self,login_act_no,login_pin):
        if login_act_no in self.accounts:
            if self.accounts[login_act_no][0]==login_pin:
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                From="singamsetty.lasya@gmail.com"
                password="nztk qphi stzd awhz"
                to="bunny.1947k@gmail.com"
                server.login(From,password)
                otp=random.randint(100000,999999)
                subject="OTP for your bank login"
                info="use this otp for your login:" +str(otp)
                msg=MIMEText(info)
                msg["from"]=From
                msg["subject"]=subject
                msg["to"]=to
                server.sendmail(From,to,msg.as_string())
                print("success")
                userotp=input("to login use the the 6 digit otp you recieved")
                if(otp==int(userotp)):
                  print("succesfully login")
                else:
                    print("invalid otp")
            else:
                print("invalid pin")
        else:
            self.createaccount(account)


    def Deposit(self,pin,amount):
        if self.accounts[act_no][0]==pin:
            self.accounts[act_no][1]+=amount
            print("amount credited succefully")
        else:
            print("entered wrong pin")


    def Withdraw(self,pin,amount):
        if self.accounts[act_no][0]==pin:
            self.accounts[act_no][1]-=amount
            print("amount debited succefully")
        else:
            print("entered wrong pin")

    def Change_pin(self):
        self.pin=int(input())
        self.new_pin=int(input())
        if self.accounts[act_no][0]==pin:
            self.accounts[act_no][0]=self.new_pin
            print("pin changed succefully")
        else:
            print("enter pin was wrong")

act=Bank()
while True:
    print("1.Login\n2.Register\n3.Exit\n4.View")
    choice=int(input("Choose option :"))

    if choice==1:
        login_act_no=int(input("enter account number"))
        if login_act_no in act.accounts:
            login_pin=int(input("enter login pin"))
            act.Login(login_act_no,login_pin)
            while True:
                choose=int(input("enter your choice:\n1.Deposit\n2.Withdraw\n3.Change_pin\n4.View\n5.Logout:"))
                if choose==1:
                    pin=int(input("enter pin:"))
                    amount=int(input("enter amount:"))
                    act.Deposit(pin,amount)
                elif choose==2:
                    pin=int(input("enter pin:"))
                    amount=int(input("enter amount:"))
                    act.Withdraw(pin,amount)
                elif choose==3:
                    act.Change_pin()
                elif choose==4:
                    print(act.accounts[act_no])
                elif choose==5:
                    break
        else:
            print("account not exist")
    elif choice==2:
        act_no=int(input("Create four digits act_no:"))
        pin=int(input("enter pin:"))
        Balance=int(input("enter balance:"))
        act.Create_Act(act_no,pin,Balance)
    elif choice==3:
        break

    elif choice==4:
        print(act.accounts)

