import json

class Book:
    def __init__(self,ISBN,book,author,is_borrowed=False):
        self.ISBN = ISBN
        self.book = book
        self.author = author
        self.is_borrowed = is_borrowed
    
    def dictionary(self):
        return{
            "ISBN":self.ISBN,
            "book":self.book,
            "author":self.author,
            "Is_borrowed":self.is_borrowed
        }
    
    def display(self):
        status="borrowed" if self.is_borrowed else  "avalible"
        print(f"ISBN: {self.ISBN}, book: {self.book} , aurthor: {self.author} status: {status}")

class Library:
    def __init__(self):
        self.books=[]
    
    def add_book(self, ISBN, title, author):
        for i in self.books:
            if i.ISBN == ISBN:
                print("Book with this ISBN already exists.")
                return
        book = Book(ISBN, title, author)
        self.books.append(book)
        print("Book added successfully.")

    def remove_book(self, ISBN):
        for i in self.books:
            if i.ISBN == ISBN:
                self.books.remove(i)
                print("book removed")
                return
        print("book not found")

    def borrow_book(self,ISBN):
        for i in self.books:
            if i.ISBN == ISBN:
                if i.is_borrowed:
                    print("book is already borrowed")
                else:
                    i.is_borrowed=True
                    print("book was Borrowed!")
                return
        print("book not found")

    def return_book(self,ISBN):
        for i in self.books:
            if i.ISBN == ISBN:
                if not i.is_borrowed:
                    print("Book was not borrowed.")
                else:
                    i.is_borrowed = False
                    print("Book returned successfully.")
                return
        print("Book not found.")

    def search_book(self,ISBN):
        for i in self.books:
            if i.ISBN == ISBN:
                print("book was found")
                return
        print("book was not found")


def main():
    library=Library()
    while True:
        print("1 to add book")
        print("2 to remove book")
        print("3 to borrow book")
        print("4 to return book")
        print("5 to search book")
        print("6 for exist")
        choice=input("enter your choice: ")

        if choice =="1":

            isbn=input("enter ISBN")
            title=input("enter title")
            author=input("enter author name")
            library.add_book(isbn,title,author)

        elif choice =="2":
            isbn=input("enter ISBN")
            library.remove_book(isbn)
            
        elif choice == "3":
            isbn = input("Enter ISBN: ")
            library.borrow_book(isbn)

        elif choice == "4":
            isbn = input("Enter ISBN: ")
            library.return_book(isbn)

        elif choice == "5":
            isbn = input("Enter ISBN: ")
            library.search_book(isbn)

        elif choice=="6":
            print("exiting program")
            break

if __name__ == "__main__":
    main()