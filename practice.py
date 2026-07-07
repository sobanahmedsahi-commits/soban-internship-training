class Book:
    def __init__(self, title, author, isbn):
        self.title = title        # attribute
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):             # method
        self.is_available = False

    def return_book(self):
        self.is_available = True