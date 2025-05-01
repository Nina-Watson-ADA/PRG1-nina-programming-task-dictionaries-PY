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
    return [book for book in library if book['title'] == search_term]


def display_loan_totals():
    on_loan = sum(1 for book in library if book["isLoaned"])
    not_on_loan = sum(1 for book in library if not book["isLoaned"])
    print(f"Total books on loan: {on_loan}")
    print(f"Total books not on loan: {not_on_loan}")

def alter_book_status(book_title, new_status):
    for book in library:
        if book["title"] == book_title:
            book["isLoaned"] = new_status
            break


def add_new_book(library, title, author, is_loaned):
    new_book = {
        "title": title,
        "author": author,
        "isLoaned": is_loaned
    }
    library.append(new_book)


def remove_book(library, book_title):
    for i, book in enumerate(library):
        if book["title"] == book_title:
            del library[i]
            return library
    return library




# Example usage
author_name = "Suzanne Collins"
books_status = get_books_by_author(library, author_name)

print(f"Books by {author_name}:")
print(books_status)

loan_status(library)