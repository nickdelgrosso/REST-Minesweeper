from fastapi.testclient import TestClient

from api.app import app


def test_ping_works():
    client = TestClient(app)
    r = client.get("/")
    assert r.ok
    msg = r.json()
    assert 'message' in msg
