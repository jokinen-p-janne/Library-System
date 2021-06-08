import pytest

from project import create_app, db
from project.models import User, Role, Book


@pytest.fixture(scope='session')
def test_client():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            db.create_all()

            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def new_test_customer():
    customer = User(firstname="Lassi", lastname="Lainaaja", username="abcd0")
    customer.roles.append(Role(name='customer'))

    customer.set_password("Password1234")

    return customer


@pytest.fixture(scope='module')
def new_test_administrator():
    administrator = User(firstname="Anssi", lastname="Admin", username="anssi.admin")
    administrator.roles.append(Role(name='administrator'))

    administrator.set_password("Password1234")

    return administrator


@pytest.fixture(scope='module')
def new_book():
    book = Book("123456789", "Test Title", "Test Author")

    return book
