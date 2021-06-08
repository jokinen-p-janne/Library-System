from project.models import Book


def test_new_book():
    book = Book(title="test title", author="test author")

    assert book.title == "test title"
    assert book.author == "test author"
