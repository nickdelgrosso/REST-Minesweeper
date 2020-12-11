from data.inmemory import Session
from domain.entities import Team


def test_session_knows_if_team_id_exists():
    team = Team(name='hi', id='abcde')
    session = Session(teams=[team], games=[])
    assert session.get_team(id='abcde') == team
    assert session.get_team(id='aaaaa') is None