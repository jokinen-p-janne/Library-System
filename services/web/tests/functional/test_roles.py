from tests.fixtures import new_test_administrator, new_test_customer  # noqa:F401


def test_new_administrator(new_test_administrator):  # noqa:F811
    administrator = new_test_administrator

    assert administrator.firstname == "Anssi"


def test_new_customer(new_test_customer):  # noqa:F811
    customer = new_test_customer

    assert customer.firstname == "Lassi"
