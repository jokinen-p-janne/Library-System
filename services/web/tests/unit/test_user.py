# from werkzeug.security import generate_password_hash

from project.models import User


def test_new_user():
    user = User(firstname="Testi", lastname="Testaaja", username="abcd0")

    user.set_password("TestPassword1234")

    assert user.firstname == "Testi"
    assert user.lastname == "Testaaja"
    assert user.username == "abcd0"
    # FIXME password hashing needs secret key
    # assert user.password_hash == generate_password_hash("TestPassword1234")
