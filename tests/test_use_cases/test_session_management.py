import pytest

from data.inmemory import Session
from minesweeper.cases.reset_session import ResetSessionUseCase, ResetRequest
from minesweeper.entitites import Team


@pytest.fixture
def session():
    session = Session()
    session.add_team(team=Team(name="test"))
    assert len(session.teams) == 1
    return session


def test_session_does_not_reset_when_credentials_incorrect(session):
    use_case = ResetSessionUseCase(session=session)
    response = use_case(request=ResetRequest(
        username="nickdg",
        password="flipthetable2",
    ))
    assert response.successful is False
    assert len(session.teams) == 1


def test_session_resets_with_correct_credentials(session):
    use_case = ResetSessionUseCase(session=session)
    response = use_case(request=ResetRequest(
        username="nickdg",
        password="flipthetable",
    ))
    assert response.successful is True
    assert len(session.teams) == 0
