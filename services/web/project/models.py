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

    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))

    password_hash = db.Column(db.String(128))

    roles = db.relationship('Role', secondary='user_roles')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User({self.username})>'


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

    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<Book("{self.title}" by {self.author})>'
