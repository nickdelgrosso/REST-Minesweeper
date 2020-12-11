import requests


def test_teams_can_register():
    r = requests.post(
        "http://localhost:8000/register",
        json={
            "team_name": "TestTeam",
        }
    )
    assert r.ok
    data = r.json()
    assert data['is_registered'] is False
    assert data['team_name'] == "TestTeam"
    assert len(data['team_id']) >= 8 and isinstance(data['team_id'], str)


def test_teams_get_unique_ids():
    r = requests.post(
        "http://localhost:8000/register",
        json={
            "team_name": "TestTeam1",
        }
    )
    r2 = requests.post(
        "http://localhost:8000/register",
        json={
            "team_name": "TestTeam1",
        }
    )
    t1, t2 = r.json(), r2.json()
    assert t1['team_name'] == t2['team_name']
    assert t1['team_id'] != t2['team_id']


def test_teams_are_registered():
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
    teams = r.json()['teams']
    assert len(teams) > 0
    assert teams[-1]['name'] == "My Team"