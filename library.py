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

  
