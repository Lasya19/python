from abc import ABC,abstractmethod

class Contact_management(ABC):
    
    @abstractmethod
    def Add_contact(self, name, phone_no):
     self.name = name
     self.phone_no = phone_no
     file = open("contact.csv", "a")
     file.write(f"{self.name},{self.phone_no}\n")
     print("success")


    def View(self):
     return obj.contacts


def Change_name(self, old_name, new_name):
    pass
    
class Contacts(Contact_management):
    contacts={}
    def Add_contact(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        if self.name not in self.contacts and self.phone_no not in self.contacts.values():
            self.contacts[self.name]=self.phone_no
            print(f"{self.name} contact created successfully")
        else:
            print("name or phone number already exists")
        

    def View(self):
        return obj.contacts
    
    def Change_name(self,old_name,new_name):
        pass


obj=Contacts()
while True:
    n=int(input("1.Create contact\n2.view contact\n3.exist"))
    if n==1:
        name=input()
        phone=int(input())
        obj.Add_contact(name,phone)
    elif n==2:
        print(obj.View())
    elif n==3:
        break