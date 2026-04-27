import pytest

from bookstore.book import Book
from bookstore.book_repository import InMemoryBookRepository
from bookstore.services.book_filtering_service import BookFilterService
from bookstore.services.bookstore_service import BookStoreService


# TODO: Create a fixture that returns a BookService instance
def create_book_service():
    """
    INSTRUCTIONS:
    - Create and return a BookService instance
    - Use InMemoryBookRepository for storage
    - Use default BookFilterService
    
    HINTS:
    """
    repository = InMemoryBookRepository()
    book_filter_service = BookFilterService()
    return BookStoreService(repository, book_filter_service)



# TODO: Create a fixture that returns a sample book for testing
def create_sample_book():
    """
    INSTRUCTIONS:
    - Create a Book instance with sample data
    - Use realistic values for title, author, genre, and price
    
    REQUIREMENTS:
    - Book should have valid, testable attributes
    """
    book = Book("Pride and Prejudice", "Jane Austen", "Romance", 35.5)
    return book



# INFO: For the following tests, use only the BookService instance created by the fixture
def test_add_book():
    """
    TESTING OBJECTIVES:
    1. Create a book service using the fixture
    2. Create a sample book using the fixture
    3. Add the book to the service
    4. Verify:
       - Book has a non-None ID
       - Book attributes match the original book
    
    HINTS:
    - Use assertions to check book details
    - Verify ID is automatically assigned
    """
    # Your implementation here
    book_service = create_book_service()
    book1 = create_sample_book()
    book_service.add(book1)
    assert book1.id is not None
    assert book1.title == "Pride and Prejudice"
    assert book1.author == "Jane Austen"
    assert book1.genre == "Romance"
    assert book1.price == 35.5


def test_add_book_validation():
    """
    TESTING OBJECTIVES:
    1. Attempt to add a book with invalid data
    2. Verify appropriate exception is raised
    
    REQUIREMENTS:
    - Test scenarios like:
      * Book with empty title
      * Book with empty author
    
    HINTS:
    - Use pytest.raises() to check for exceptions
    """
    # Your implementation here
    book_service = create_book_service()
    invalid_book = Book ("Persuasion", "", "Romance", 30)
    with pytest.raises(ValueError):
        book_service.add(invalid_book)   
    
    invalid_book2 = Book ("", "Jane Austen", "Romance", 30.5)
    with pytest.raises(ValueError):
        book_service.add(invalid_book2)


# INFO: Here you should use @pytest.mark.parametrize to test multiple genres
@pytest.mark.parametrize("test_genre, expected_count", [("Romance", 1), ("Dystopian", 1), ("Sci-Fi", 1), ("Horror", 1)] )
def test_get_books_by_genre():
    """
    TESTING OBJECTIVES:
    1. Add multiple books with different genres
    2. Filter books by specific genres
    3. Verify:
       - Only books of the specified genre are returned
       - Filtering is case-insensitive
    
    REQUIREMENTS:
    - Add books across multiple genres
    - Test filtering with different genre inputs
    
    HINTS:
    - Use service's get_books() method with genre parameter
    - Check length and genre of returned books
    """
    # Your implementation here
    book_service = create_book_service()
    book1 = Book ("Persuasion", "Jane Austen", "Romance", 30.5)
    book2 = Book ("1985", "George Orwell", "Dystopian", 20)
    book3 = Book ("Foundation", "Isaac Asimov", "Sci-Fi", 40)

    book_service.add(book1)
    book_service.add(book2)
    book_service.add(book3)

    results = book_service.get_books(genre=test_genre)

# INFO: Here you should use @pytest.mark.parametrize to test multiple price ranges
def test_price_range_filtering():
    """
    TESTING OBJECTIVES:
    1. Add books at different price points
    2. Test filtering by:
       - Minimum price
       - Maximum price
       - Combined price range
    
    REQUIREMENTS:
    - Verify correct number of books returned
    - Ensure only books within price range are included
    
    HINTS:
    - Add books with varied prices
    - Use get_books() with min_price and max_price
    - Test edge cases and different price combinations
    """
    # Your implementation here
    pass


def test_update_book():
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Update the book's details
    3. Verify:
       - Specific attributes can be updated
       - Updated values are correct
       - Other attributes remain unchanged
    
    REQUIREMENTS:
    - Test updating multiple attributes
    - Ensure update works for different book properties
    
    HINTS:
    - Use update_book() method
    - Compare book before and after update
    """
    # Your implementation here
    pass


def test_remove_book():
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Remove the book
    3. Verify:
       - Book is successfully removed
       - Attempting to retrieve the book returns None
    
    REQUIREMENTS:
    - Test successful book removal
    - Test removing a non-existent book
    
    HINTS:
    - Use remove_book() method
    - Check return value of remove operation
    - Verify book is no longer in the service
    """
    # Your implementation here
    pass
