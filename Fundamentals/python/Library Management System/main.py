class Book:
    def __init__(self, book_id, title, author, year, status):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status.lower()

    def display(self):
        print(
            f"--------------------\n"
            f"ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Year: {self.year}\n"
            f"Availability: {self.status}\n"
            f"--------------------"
        )


class Member:
    def __init__(self, member_id, name, email):
        self.id = member_id
        self.name = name
        self.email = email

    def display(self):
        print(
            f"--------------------\n"
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"--------------------"
        )


class Library:
    def __init__(self):
        self.books = []
        self.members = []

   
    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def add_book(self):
        n = int(input("No. of books to add: "))

        for _ in range(n):
            book_id = input("ID: ")

            if self.find_book(book_id):
                print("Book already exists!")
                continue

            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            status = input("Availability (yes/no): ")

            self.books.append(
                Book(book_id, title, author, year, status)
            )

            print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            book.display()

    def search_book(self):
        search_by = input(
            "Search by (id/title/author): "
        ).lower()

        if search_by not in ["id", "title", "author"]:
            print("Invalid search option.")
            return

        value = input("Search for: ").lower()

        found = False

        for book in self.books:
            if value in getattr(book, search_by).lower():
                book.display()
                found = True

        if not found:
            print("Book not found.")

    def borrow_book(self):
        book_id = input("Enter Book ID: ")

        book = self.find_book(book_id)

        if not book:
            print("Book not found.")
            return

        if book.status == "yes":
            book.status = "no"
            print("Book borrowed successfully.")
        else:
            print("Book is not available.")

    def return_book(self):
        book_id = input("Enter Book ID: ")

        book = self.find_book(book_id)

        if not book:
            print("Book not found.")
            return

        if book.status == "no":
            book.status = "yes"
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def delete_book(self):
        book_id = input("Enter Book ID: ")

        book = self.find_book(book_id)

        if not book:
            print("Book not found.")
            return

        self.books.remove(book)
        print("Book deleted successfully.")

    def view_borrowed_books(self):
        borrowed = [book for book in self.books if book.status == "no"]

        if not borrowed:
            print("No books are borrowed.")
            return

        for book in borrowed:
            book.display()

   

    def add_members(self):
        n = int(input("No. of members to add: "))

        for _ in range(n):
            member_id = input("ID: ")

            exists = any(
                member.id == member_id
                for member in self.members
            )

            if exists:
                print("Member already exists!")
                continue

            name = input("Name: ")
            email = input("Email: ")

            self.members.append(
                Member(member_id, name, email)
            )

            print("Member added successfully!")

    def view_members(self):
        if not self.members:
            print("No members available.")
            return

        for member in self.members:
            member.display()




lib = Library()

while True:
    print("""
LIBRARY MANAGEMENT SYSTEM

1. Add Book
2. View Books
3. Search Book
4. Add Members
5. View Members
6. Borrow Book
7. Return Book
8. Delete Book
9. View Borrowed Books
10. Exit
""")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        lib.add_book()

    elif choice == 2:
        lib.view_books()

    elif choice == 3:
        lib.search_book()

    elif choice == 4:
        lib.add_members()

    elif choice == 5:
        lib.view_members()

    elif choice == 6:
        lib.borrow_book()

    elif choice == 7:
        lib.return_book()

    elif choice == 8:
        lib.delete_book()

    elif choice == 9:
        lib.view_borrowed_books()

    elif choice == 10:
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice.")

    
    


                      









    
  

   
    
       
    
    

        
