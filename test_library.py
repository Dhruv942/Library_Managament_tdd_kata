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
if __name__ == '__main__':
    unittest.main()