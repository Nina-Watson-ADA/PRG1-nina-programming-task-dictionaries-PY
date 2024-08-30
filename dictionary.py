library = [
    {
        "title": "The Road Ahead",
        "author": "Bill Gates",
        "isLoaned": True
    },
    {
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "isLoaned": True
    },
    {
        "title": "Mockingjay: The Final Book of The Hunger Games",
        "author": "Suzanne Collins",
        "isLoaned": False
    }
]


def loan_status(lib):
    for book in lib:
        book_info = f"{book['title']} by {book['author']}"

        if book["isLoaned"]:
            print(f"Out on loan: {book_info}")
        else:
            print(f"On the shelf: {book_info}")


def get_books_by_author(library, author_name):
    books_by_author = []

    for book in library:
        if book["author"] == author_name:
            book_status = "Out on loan" if book["isLoaned"] else "On the shelf"
            books_by_author.append(f"{book['title']} - {book_status}")

    return books_by_author


def search_by_book_name(library, search_term):
    pass


def display_loan_totals():
    pass


def alter_book_status(book_title, new_status):
    pass


def add_new_book(library, title, author, is_loaned):
    pass


def remove_book(library, book_title):
    pass




# Example usage
author_name = "Suzanne Collins"
books_status = get_books_by_author(library, author_name)

print(f"Books by {author_name}:")
print(books_status)

loan_status(library)