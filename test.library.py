import unittest
from library import Library, Book

class LibraryTestCase(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_single_book(self):
       
        book = Book(isbn='1234567890', title='Test-Driven Development', author='xyz', year=2002)
        self.library.add_book(book)
        self.assertEqual(self.library.books[0].isbn, '1234567890')

if __name__ == '__main__':
    unittest.main()