from django.test import Client


def test_index():
    client = Client()
    response = client.get('/app2_1/')

    assert response.status_code == 200
