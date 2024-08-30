import pytest
from dictionary import library, loan_status, get_books_by_author, search_by_book_name, display_loan_totals, alter_book_status, add_new_book, remove_book

@pytest.fixture
def library_fixture():  # Define a fixture to provide the library
    return library.copy()  # Return a copy to avoid modifying the original

@pytest.fixture
def clean_library(library_fixture):
    original_library = library_fixture.copy()
    yield original_library

# Helper function to capture print output
def capture_print_output(func, *args, **kwargs):
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()


def test_loan_status():
    test_library = [
        {"title": "Book 1", "author": "Author 1", "isLoaned": True},
        {"title": "Book 2", "author": "Author 2", "isLoaned": False},
    ]
    output = capture_print_output(loan_status, test_library)
    assert "Out on loan: Book 1 by Author 1" in output
    assert "On the shelf: Book 2 by Author 2" in output


def test_get_books_by_author(clean_library):
    author_name = "Bill Gates"
    result = get_books_by_author(clean_library, author_name)

    assert isinstance(result, list)
    assert "The Road Ahead - Out on loan" in result

    author_name = "Nonexistent Author"
    result = get_books_by_author(clean_library, author_name)

    assert isinstance(result, list)
    assert len(result) == 0


# Tests for additional tasks
def test_search_by_book_name(clean_library):
    result1 = search_by_book_name(clean_library, "The Road Ahead")
    result2 = search_by_book_name(clean_library, "Mockingjay: The Final Book of The Hunger Games")
    result3 = search_by_book_name(clean_library, "Nonexistent Book")

    assert isinstance(result1, list)
    assert len(result1) == 1
    assert result1[0] == {"title": "The Road Ahead", "author": "Bill Gates", "isLoaned": True} 

def test_display_loan_totals():
    output = capture_print_output(display_loan_totals)
    assert "Total books on loan: 2" in output
    assert "Total books not on loan: 1" in output


def test_alter_book_status():
    book_to_alter = next((book for book in library if book["title"] == "The Road Ahead"), None)
    original_status = book_to_alter["isLoaned"]

    alter_book_status("The Road Ahead", not original_status)

    assert book_to_alter["isLoaned"] == (not original_status)


def test_add_new_book(clean_library):  # Use the clean_library fixture
    original_length = len(clean_library)

    add_new_book(clean_library, "New Book", "New Author", False)  # Pass the clean library to add_new_book

    assert len(clean_library) == original_length + 1
    assert clean_library[-1] == {
        "title": "New Book",
        "author": "New Author",
        "isLoaned": False
    }


def test_remove_book(clean_library):
    original_length = len(clean_library)

    updated_library = remove_book(clean_library, "Steve Jobs")

    assert len(updated_library) == original_length - 1
    assert not any(book["title"] == "Steve Jobs" for book in updated_library)  # Check updated_library