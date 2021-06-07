from project import db
from project.models import Loan
from tests.fixtures import new_customer, new_employee, new_book  # noqa:F401


def test_new_loan(new_book, new_customer, new_employee):  # noqa:F811
    book = new_book
    customer = new_customer
    employee = new_employee

    db.session.add(book)
    db.session.add(customer)
    db.session.add(employee)

    db.session.commit()

    loan = Loan(book.id, customer.id, employee.id)

    assert loan

    db.session.add(loan)

    db.session.commit()

    loans = customer.loans.all()

    assert loans
