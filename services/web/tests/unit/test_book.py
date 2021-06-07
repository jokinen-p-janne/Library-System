from project.models import Book


def test_new_book():
    book = Book('12345', "test", "test")

    assert book.author == "test"
