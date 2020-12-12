from fastapi.testclient import TestClient

from src.api import app


def test_ping_works():
    client = TestClient(app)
    r = client.get("/")
    assert r.ok
    msg = r.json()
    assert 'message' in msg
