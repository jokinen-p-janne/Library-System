from tests.fixtures import test_client  # noqa:F401


def test_index(test_client):  # noqa:F811
    response = test_client.get('/')

    assert response.status_code == 200

    response = test_client.get('/index')

    assert response.status_code == 200
