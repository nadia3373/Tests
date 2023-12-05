import unittest
from unittest.mock import Mock

from book.book_repository import BookRepository
from book.book import Book
from book.book_service import BookService


class TestBookService(unittest.TestCase):
    def test_find_book_by_id(self):
        mock_repository = Mock(spec=BookRepository)
        mock_repository.find_by_id.return_value = Book("1", "Book1", "Author1")
        book_service = BookService(mock_repository)

        result = book_service.find_book_by_id("1")

        self.assertEqual(result.title, "Book1")
        self.assertEqual(result.author, "Author1")

    def test_find_all_books(self):
        mock_repository = Mock(spec=BookRepository)
        mock_repository.find_all.return_value = [
            Book("1", "Book1", "Author1"),
            Book("2", "Book2", "Author2"),
        ]
        book_service = BookService(mock_repository)

        result = book_service.find_all_books()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, "Book1")
        self.assertEqual(result[1].title, "Book2")
