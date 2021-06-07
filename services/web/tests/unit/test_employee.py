from werkzeug.security import check_password_hash

from project.models import Employee


def test_new_employee():
    employee = Employee("Testi", "Testaaja", "TestPassword1234")

    assert employee.firstname == "Testi"
    assert employee.lastname == "Testaaja"
    assert check_password_hash(employee.password_hash, "TestPassword1234")
