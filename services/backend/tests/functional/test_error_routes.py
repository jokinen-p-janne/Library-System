from tests.fixtures import test_client  # noqa:F401


def test_404_error(test_client):  # noqa:F811
    response = test_client.get('/notfound')

    assert response.status_code == 404
    assert b"Not found" in response.data
