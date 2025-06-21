class Book:
    """Represents a book with a title, author, and checked-out status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Already available

    def is_available(self):
        """Check if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books and allows operations on them."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title if it's currently checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is not checked out or not found.")

    def list_available_books(self):
        """Print all books in the library that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")