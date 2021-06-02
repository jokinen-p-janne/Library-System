from project import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(128), unique=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
