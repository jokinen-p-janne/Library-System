from werkzeug.security import generate_password_hash, check_password_hash

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


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

        self.set_password(password)

    def __repr__(self):
        return f'<Customer({self.firstname} {self.lastname} {self.email})'


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128), nullable=False)
    lastname = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, firstname, lastname, password):
        self.firstname = firstname
        self.lastname = lastname

        self.set_password(password)

    def __repr__(self):
        return f'<Employee({self.firstname} {self.lastname})'
