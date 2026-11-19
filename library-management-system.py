file = open("library.csv", "w")
file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
file.close()
file = open("students.csv", "w")
file.write("STUDENT_ID,PASSWORD,BOOK_ID,BOOK_TAKEN\n")
file.close()
class Library():
    Books = {}
    Librarian = {}
    Students = {}
    def Create_lib_Account(self):
        username = input("Username: ")
        if username in Library.Librarian:
            print("account already exists")
        else:    
           password = input("Password: ")
           Library.Librarian[username] = password
           print("Librarian Account Created Successfully")
    def Create_student_Account(self):
        std_id = int(input("Student ID: "))
        password = input("Password: ")
        if std_id not in Library.Students:
            Library.Students[std_id] = [password, None, None]
            file = open("students.csv", "a")
            file.write(f"{std_id},{password},None,None\n")
            file.close()
            print("Student Account Created Successfully")
        else:
            print("Student Account Already Exists")
    def Add_Book(self, book_id, name, author):
        if book_id not in Library.Books:
            self.book_id = book_id
            self.name = name
            self.author = author
            availability = True
            Library.Books[book_id] = [self.name, self.author, availability]
            file = open("library.csv", "a")
            file.write(f"{book_id},{self.name},{self.author},{availability}\n")
            file.close()
            print("Success")
        else:
            print("Book already exists")
    def Display_Books(self):
        file = open("library.csv", "r")
        data = file.read()
        file.close()
        print(data)
    def Search_Book(self, book_id):
        if book_id in Library.Books:
            self.title = Library.Books[book_id][0]
            self.author = Library.Books[book_id][1]
            self.available = Library.Books[book_id][2]
            if self.available:
                self.status = "Yes"
            else:
                self.status = "No"
            print(f"Book Id:{book_id}, Title:{self.title}, Author:{self.author}, Availability:{self.status}")
        else:
            print("The book is not in library")
    def Issue_Book(self, book_id, std_id):
        if Library.Students[std_id][1] == None:
            if book_id in Library.Books:
                if Library.Books[book_id][2] == True:
                    Library.Books[book_id][2] = False
                    Library.Students[std_id][1] = book_id
                    Library.Students[std_id][2] = Library.Books[book_id][0]
                    print("Book issued successfully")
                    file = open("library.csv", "w")
                    file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
                    for i, j in Library.Books.items():
                        file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
                    file.close()
                    file = open("students.csv", "w")
                    file.write("STUDENT_ID,PASSWORD,BOOK_ID,BOOK_TAKEN\n")
                    for i, j in Library.Students.items():
                        file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
                    file.close()
                else:
                    print("Book is already issued to someone")
            else:
                print("Book not in library")
        else:
            print("You were already issued a book")
    def Return_Book(self, std_id):
        if Library.Students[std_id][1] is not None:
            book_id = Library.Students[std_id][1]
            Library.Books[book_id][2] = True
            Library.Students[std_id][1] = None
            Library.Students[std_id][2] = None
            print("Book returned successfully")
            file = open("library.csv", "w")
            file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
            for i, j in Library.Books.items():
                file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
            file.close()
            file = open("students.csv", "w")
            file.write("STUDENT_ID,PASSWORD,BOOK_ID,BOOK_TAKEN\n")
            for i, j in Library.Students.items():
                file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
            file.close()
        else:
            print("You don't have any books issued")
    def Delete_Book(self, book_id):
        if book_id in Library.Books:
            if Library.Books[book_id][2] == False:
                print("the book is currently issued cannot be deleted")
                return
            del Library.Books[book_id]
            print("Book deleted successfully")
            file = open("library.csv", "w")
            file.write("BOOK_ID,NAME,AUTHOR,AVAILABILITY\n")
            for i, j in Library.Books.items():
                file.write(f"{i},{j[0]},{j[1]},{j[2]}\n")
            file.close()
        else:
            print("Book is not in library")
l1 = Library()
while True:
    choice = int(input("1. Librarian Login\n""2. Create Librarian Account\n""3. Exit\n""Enter your choice: "))
    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in Library.Librarian:
            if Library.Librarian[username] == password:
                print("Librarian logged in successfully")
                while True:
                    command = int(input("\n1. Add Book\n""2. Display Books\n""3. Search for a Book\n""4. Issue Book\n""5. Return Book\n""6. Delete Book\n""7. Create Student Account\n""8. Logout\n""Enter your choice: "))
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
                        std_id = int(input("Enter Student ID: "))
                        if std_id in Library.Students:
                            password = input("Enter Student Password: ")
                            if Library.Students[std_id][0] == password:
                                book_id = int(input("Enter Book ID: "))
                                l1.Issue_Book(book_id, std_id)
                            else:
                                print("Wrong Student Password")
                        else:
                            print("Student account does not exist")
                    elif command == 5:
                        std_id = int(input("Enter Student ID: "))
                        if std_id in Library.Students:
                            password = input("Enter Student Password: ")
                            if Library.Students[std_id][0] == password:
                                l1.Return_Book(std_id)
                            else:
                                print("Wrong Student Password")
                        else:
                            print("Student account does not exist")
                    elif command == 6:
                        book_id = int(input("Enter Book ID: "))
                        l1.Delete_Book(book_id)
                    elif command == 7:
                        l1.Create_student_Account()
                    elif command == 8:
                        print("Librarian logged out")
                        break
                    else:
                        print("Invalid choice")
            else:
                print("Incorrect Librarian Password")
        else:
            print("Librarian account does not exist")
            print("create an account")
            l1.Create_lib_Account()
    elif choice == 2:
        l1.Create_lib_Account()
    elif choice == 3:
        print("Exited")
        break
    else:
        print("Invalid choice")