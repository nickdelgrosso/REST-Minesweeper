import pytest
import requests


def test_ping_works():
    r = requests.get("http://localhost:8000")
    assert r.ok
    msg = r.json()
    assert 'message' in msg



#
# def test_new_game_can_be_started():
#     r = requests.post(
#         "http://localhost:8000/reset",
#         json={
#             "username": "nickdg",  # NEVER HARDCODE USERNAMES AND PASSWORDS, ESP. INTO TESTS!!!
#             "password": "flipthetable",
#
#         }
#     )
#     assert r.ok
#     r = requests.post(
#         "http://localhost:8000/register",
#         json={
#             "team_name": "My Team",
#             "do_registration": True,
#         }
#     )
#     assert r.ok
#     data = r.json()
#     team_name, team_id = data['team_name'], data['team_id']
#     r = requests.post(
#         "http://localhost:8000/new-game",
#         json={
#             "team_id": team_id,
#             "n_stones": 4,
#         }
#     )
#     assert r.ok
