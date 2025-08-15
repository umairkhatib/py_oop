# Book class demonstrates the use of class variables and class methods
class Book:
    """
    Book class with:
    - a class variable 'total_books' to track the number of books
    - a class method 'increment_book_count' to increase the count
    """

    # Class variable: shared among all instances
    total_books = 0

    def __init__(self, title, author):
        """
        Constructor to initialize book title and author
        and automatically increment total_books using the class method.
        """
        self.title = title      # Instance variable
        self.author = author    # Instance variable
        Book.increment_book_count()  # Increment the class variable

    @classmethod
    def increment_book_count(cls):
        """
        Class method to increase the total_books count.
        cls refers to the class itself.
        """
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        """
        Class method to display total number of books.
        """
        print(f"Total books: {cls.total_books}")


# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Alchemist", "Paulo Coelho")

# Access class method
Book.display_total_books()  # Output: Total books: 3

# Access class variable directly
print(Book.total_books)     # Output: 3
