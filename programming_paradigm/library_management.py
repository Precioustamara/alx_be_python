class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f'You have successfully checked out "{title}".'
                else:
                    return f'The book "{title}" is already checked out.'
            else:
                return f'The book "{title}" is not in the library.'

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f'You have successfully returned "{title}".'
                else:
                    return f'The book "{title}" was not checked out.'
            else:
                return f'The book "{title}" is not in the library.'


def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return "Available books: " + ", ".join(available_books)
        return "No books are currently available."

# library = Library()

# book1 = Book("1984", "George Orwell")
# book2 = Book("To Kill a Mockingbird", "Harper Lee")
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# #print(library.list_available_books(book1, book2, book3)) # Lists all books
# print(library.check_out_book("1984"))  # Checks out "1984"
# #print(library.list_available_books())  # Lists available books after checkout
# print(library.return_book("1984"))     # Returns "1984"
#print(library.list_available_books()) 