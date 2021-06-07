import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from project import db, login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    roles = db.relationship('Role', secondary='user_roles')
    loans = db.relationship('Loan', backref='customer', lazy='dynamic')
    reservations = db.relationship('Reservation', backref='customer', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(128), unique=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)

    loan = db.relationship('Loan', backref='loaner', lazy='dynamic')

    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def __repr__(self):
        return f'<Book("{self.title}" by {self.author.firstname} {self.author.lastname})>'


class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    loan_date = db.Column(db.DateTime)
    return_date = db.Column(db.DateTime)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, book_id, customer_id, employee_id):
        self.loan_date = datetime.datetime.now()
        self.return_date = datetime.datetime.now() + datetime.timedelta(days=30)
        self.book_id = book_id
        self.user_id = user_id

    def __repr__(self):
        return f'<Loan({self.book_id} {self.customer_id} {self.employee_id})>'


class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    reservation_date = db.Column(db.DateTime)
    pickup_date = db.Column(db.DateTime)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __init__(self, book_id, customer_id, employee_id):
        self.reservation_date = datetime.datetime.now()
        self.pickup_date = datetime.datetime.now() + datetime.timedelta(days=14)
        self.book_id = book_id
        self.customer_id = customer_id
        self.employee_id = employee_id

    def __repr__(self):
        return f'<Reservation({self.book_id} {self.customer_id} {self.emplyee_id})>'
