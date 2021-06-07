import pytest

from project import create_app, db
from project.models import Customer, Employee, Book


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
def new_customer():
    customer = Customer("Testi", "Testaaja", "testi.testaaja@test.com", "TestPassword1234")

    return customer


@pytest.fixture(scope='module')
def new_employee():
    employee = Employee("Testi", "Testaaja", "TestPassword1234")

    return employee


@pytest.fixture(scope='module')
def new_book():
    book = Book("123456789", "Test Title", "Test Author")

    return book
