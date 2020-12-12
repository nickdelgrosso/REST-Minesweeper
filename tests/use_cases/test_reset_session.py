import pytest

from src.repo import Session
from src.use_cases.reset_session import ResetSessionUseCase, ResetRequest
from src.domain import Team


@pytest.fixture
def session():
    session = Session()
    session.add_team(team=Team(name="test"))
    assert len(session.teams) == 1
    return session


def test_session_does_not_reset_when_credentials_incorrect(session):
    reset_session = ResetSessionUseCase(session=session)
    response = reset_session(request=ResetRequest(
        username="nickdg",
        password="flipthetable2",
    ))
    assert response.successful is False
    assert len(session.teams) == 1


def test_session_resets_with_correct_credentials(session):
    reset_session = ResetSessionUseCase(session=session)
    response = reset_session(request=ResetRequest(
        username="nickdg",
        password="flipthetable",
    ))
    assert response.successful is True
    assert len(session.teams) == 0
