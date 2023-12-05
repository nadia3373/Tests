from book.book import Book


class BookRepository:
    def find_by_id(self, id):
        pass

    def find_all(self):
        pass


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {
            "1": Book("1", "Book1", "Author1"),
            "2": Book("2", "Book2", "Author2"),
        }

    def find_by_id(self, id):
        return self.books.get(id)

    def find_all(self):
        return list(self.books.values())
