from tests.fixtures import test_client  # noqa:F401


def test_register(test_client):  # noqa:F811
    response = test_client.get('/register')

    assert response.status_code == 200


def test_login(test_client):  # noqa:F811
    response = test_client.get('/login')

    assert response.status_code == 200


def test_logout(test_client):  # noqa:F811
    response = test_client.get('/logout')

    assert response.status_code == 302
