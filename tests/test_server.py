import pytest
import requests

def test_ping_works():
    r = requests.get("http://localhost:8000")
    assert r.ok
    msg = r.json()
    assert 'message' in msg


def teams_can_register():
    r = requests.post(
        "http://localhost:8000/register",
        data={
            "team_name": "TestTeam",
        }
    )
    assert r.ok
    