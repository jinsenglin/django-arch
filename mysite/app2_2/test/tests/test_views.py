from django.test import Client


def test_index():
    client = Client()
    response = client.get('/app2_2/')

    assert response.status_code == 200
