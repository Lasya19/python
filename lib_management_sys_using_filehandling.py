
file=open("library.csv",mode="w")
file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
file.close()
class Library():
    Books={}
    def Add_Book(self, book_id, name, author):
       file=open("library.csv",mode="a")
       if(book_id not in Library.Books): 
        self.book_id=book_id
        self.name=name
        self.author=author
        availabilty=True
        Library.Books[book_id]=[self.name,self.author,availabilty]
        file.write(f"{book_id},{self.name},{self.author},{availabilty}\n")
        print("success")
       else:
           print("Book already exists")
       file.close()     
    def Display_Books(self):
        file = open("library.csv", "r")
        data = file.read()
        file.close()
        print(data)
    def Search_Book(self,book_id):
              if book_id in Library.Books:
                 self.title=Library.Books[book_id][0]
                 self.author=Library.Books[book_id][1]
                 self.available=Library.Books[book_id][2]
                 if self.available:
                    self.status = "Yes"
                 else:
                    self.status = "No"
                 print(f"Book Id:{book_id} ,Title:{self.title} ,Author:{self.author}, Availabity:{self.status}")
              else:
                  print("the book is not in library")
    
    def Issue_Book(self, book_id):
     if book_id in Library.Books:
        if Library.Books[book_id][2] == True:
            Library.Books[book_id][2] = False
            print("Book issued successfully")
            file = open("library.csv", "w")
            file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
            for i, j in Library.Books.items():
                file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
            file.close()
        else:
            print("Book is already issued to someone")
     else:
        print("Book not in library")
    def Return_Book(self, book_id):
     if book_id in Library.Books:
        if Library.Books[book_id][2] == False:
            Library.Books[book_id][2] = True
            print("Book returned successfully")
            file = open("library.csv", "w")
            file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
            for i, j in Library.Books.items():
                file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
            file.close()
        else:
            print("Book is already returned to the library")
     else:
        print("Book not in library")        
    def Delete_Book(self, book_id):
     if book_id in Library.Books:
        del Library.Books[book_id]
        print("Book deleted successfully")
        file = open("library.csv", "w")
        file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
        for i, j in Library.Books.items():
            file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
        file.close()
     else:
        print("Book is not in library")
l1=Library()        
while True:
    command = int(input("1. Add Book\n""2. Display Books\n""3. Search for a Book\n""4. Issue Book\n""5. Return Book\n""6. Delete Book\n""7. Exit\n" "Enter your choice: "
    ))
    if command == 1:
        book_id = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        l1.Add_Book(book_id, name, author)
    elif command == 2:
        l1.Display_Books()
    elif command == 3:
        book_id = int(input("Enter Book ID: "))
        l1.Search_Book(book_id)
    elif command == 4:
        book_id = int(input("Enter Book ID: "))
        l1.Issue_Book(book_id)
    elif command == 5:
        book_id = int(input("Enter Book ID: "))
        l1.Return_Book(book_id)
    elif command == 6:
        book_id = int(input("Enter Book ID: "))
        l1.Delete_Book(book_id)
    elif command == 7:
        print("Exit")
        break
    else:
        print("Invalid choice")