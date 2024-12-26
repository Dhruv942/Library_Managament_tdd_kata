import unittest
from library import Library, Book

class LibraryTestCase(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_single_book(self):
       
        book = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
        self.library.add_book(book)
        self.assertEqual(self.library.books[0].isbn, '1234567890')

    def test_borrowbook(self):
        book = Book(isbn="1234567890", title="c++", author="bde", year=2010)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.assertTrue(book.is_borrowed)

    def test_borrow_nonexistent_book(self):
        with self.assertRaises(ValueError):
            self.library.borrow_book("xyz")

    def test_return_book(self):
        book = Book(isbn="1234567890", title="snake", author="abc", year=1958)
        self.library.add_book(book)
        self.library.borrow_book(book.isbn)
        self.library.return_book(book.isbn)
        self.assertFalse(book.is_borrowed)
    
    def test_return_book_not_borrowed(self):
        book = Book(isbn="1234567890", title="snake", author="abc", year=1958)
        self.library.add_book(book)
        with self.assertRaises(ValueError):
            self.library.return_book(book.isbn)
    

    def test_view_all_books(self):
        book1 = Book(isbn="1234567890", title="Python", author="shubhash", year=2015)
        book2 = Book(isbn="0987654321", title="Java", author="kartik", year=2020)
        self.library.add_book(book1)
        self.library.add_book(book2)
        
        all_books = [(book.isbn, book.title, book.author, book.year) for book in self.library.books]
        expected_books = [
            ("1234567890", "Python", "shubhash", 2015),
            ("0987654321", "Java", "kartik", 2020)
        ]
        
        self.assertEqual(all_books, expected_books)
             

if __name__ == '__main__':
    unittest.main()