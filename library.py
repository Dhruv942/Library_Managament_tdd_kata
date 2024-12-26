class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
    
        for b in self.books:
            if b.isbn == book.isbn:
                raise ValueError("This book is already in the library.")
        
        self.books.append(book)

    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    raise ValueError("Book is already borrowed.")
                book.is_borrowed = True
                return
        raise ValueError("Book not found in the library.")    

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    raise ValueError("Book is not borrowed.")
                book.is_borrowed = False
                return
        raise ValueError("Book not found in the library.")
    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]