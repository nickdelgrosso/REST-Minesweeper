import requests


def test_session_can_be_reset():
    r = requests.post(
        "http://localhost:8000/register",
        json={
            "team_name": "My Team",
            "do_registration": True,
        }
    )
    assert r.ok
    r = requests.get(
        "http://localhost:8000/teams",
    )
    assert r.ok
    assert len(r.json()['teams']) > 0
    r = requests.post(
        "http://localhost:8000/reset",
        json={
            "username": "nickdg",  # NEVER HARDCODE USERNAMES AND PASSWORDS, ESP. INTO TESTS!!!
            "password": "flipthetable",

        }
    )
    assert r.ok
    r = requests.get(
        "http://localhost:8000/teams",
    )
    assert r.ok
    assert len(r.json()['teams']) == 0
