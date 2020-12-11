import requests


def test_ping_works():
    r = requests.get("http://localhost:8000")
    assert r.ok
    msg = r.json()
    assert 'message' in msg
