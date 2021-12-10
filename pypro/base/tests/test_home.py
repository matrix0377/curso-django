from django.test import Client


def test_status_code(client: Client):
    client.get('/')
    assert resp.status_code == 200

