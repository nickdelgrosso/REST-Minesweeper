import requests


def test_new_game_can_be_started_with_correct_team_id():
    r = requests.post(
        "http://localhost:8000/reset",
        json={
            "username": "nickdg",  # NEVER HARDCODE USERNAMES AND PASSWORDS, ESP. INTO TESTS!!!
            "password": "flipthetable",

        }
    )
    assert r.ok
    r = requests.post(
        "http://localhost:8000/register",
        json={
            "team_name": "My Team",
            "do_registration": True,
        }
    )
    assert r.ok
    data = r.json()
    team_id = data['team_id']

    r = requests.get(
        "http://localhost:8000/teams",
    )
    assert r.ok
    teams = r.json()['teams']
    assert len(teams) > 0
    assert teams[-1]['name'] == "My Team"

    r = requests.post(
        "http://localhost:8000/new-game",
        json={
            "team_id": team_id,
            "n_stones": 4,
        }
    )
    assert r.ok
    data = r.json()
    assert data['successful'] == True
    assert isinstance(data['game_id'], str) and len(data['game_id']) >= 8
