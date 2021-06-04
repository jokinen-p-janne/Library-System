from werkzeug.security import check_password_hash

from project.models import Customer


def test_new_customer():
    customer = Customer("Testi", "Testaaja", "testi.testaaja@test.com", "TestPassword1234")

    assert customer.firstname == "Testi"
    assert customer.lastname == "Testaaja"
    assert customer.email == "testi.testaaja@test.com"
    assert check_password_hash(customer.password_hash, "TestPassword1234")
