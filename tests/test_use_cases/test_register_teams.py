import pytest

from data.inmemory import Session
from minesweeper.cases.register_team import RegisterTeamUseCase, RegistrationRequest


@pytest.fixture
def session():
    return Session()


def test_teams_can_register(session):
    assert len(session.teams) == 0
    register_team = RegisterTeamUseCase(session=session)
    register_team(RegistrationRequest(team_name="abcd"))
    assert len(session.teams) == 1
    team = session.teams[0]
    assert hasattr(team, 'id')
    assert team.name == "abcd"


def test_teams_get_unique_ids(session):
    register_team = RegisterTeamUseCase(session=session)
    register_team(RegistrationRequest(team_name="TestTeam1"))
    register_team(RegistrationRequest(team_name="TestTeam1"))
    assert len(session.teams) == 2
    t1, t2 = session.teams
    assert t1.name == t2.name
    assert t1.id != t2.id
