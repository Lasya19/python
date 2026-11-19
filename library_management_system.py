file =open("library.csv",mode="w")
class Library():
    Books={}
    def add_book(self, book_id, name, author):
        self.book_id=book_id
        self.name=name
        self.author=author
        Library.Books[book_id]=[self.name,self.author,True]
    def display_books(self):
      for i, j in Library.Books.items():
        if j[2]:
            status = "Yes"
        else:
            status = "No"
        print(f"Book ID: {i}, Name: {j[0]}, Author: {j[1]}, Availability: {status}")
    def search_book(self,book_id):
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
    def issue_book(self, book_id):
        if book_id in Library.Books:
            if Library.Books[book_id][2]==True:
                Library.Books[book_id][2]=False
                print("Book issued successfully")
            else:
                print("book is already issued to someone")
        else:
             print("book not in library")
    def return_book(self, book_id):
        if book_id in Library.Books:
            if Library.Books[book_id][2]==False:
                Library.Books[book_id][2]=True
                print("Book Returned successfully")
            else:
                print("book is already returned to the library check the book id")
        else:
             print("Book is not in library")
    def delete_book(self, book_id):
        if book_id in Library.Books:
            del Library.Books[book_id]
            print("deleted successfull")
        else:
            print("book is not in library")
l1=Library()        
l1.add_book(101, "Python", "Guido")
l1.add_book(102, "Java", "James")
l1.display_books()
#l1.search_book(101)
l1.issue_book(101)
l1.display_books()
l1.issue_book(101)
l1.return_book(101)
l1.display_books()
l1.delete_book(101)
l1.display_books()
l1.delete_book(101)
l1.display_books()







