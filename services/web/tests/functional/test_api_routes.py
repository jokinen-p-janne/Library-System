from tests.fixtures import test_client  # noqa:F401


def test_api_v1_ping(test_client):  # noqa:F811
    response = test_client.get('/api/v1/ping')

    assert response.status_code == 200
    assert b"pong" in response.data
