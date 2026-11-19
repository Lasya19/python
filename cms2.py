file=open("contact.csv","r")
info=file.readlines()
name=input("enter name:")
phone_no=int(input("enter number"))
for i in info[1:]:
    data=i.split(",")

    if data[0]!=name:
       with open("contact.csv","a") as file:
           file.write(f"{name},{phone_no}\n")
           break
    else:
        print("name already exists")
        break
    
    #create update change name 