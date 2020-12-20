import pytest

from src.repo import Session
from src.use_cases.new_game import NewGameUseCase, NewGameRequest
from src.domain.context import Team


@pytest.fixture
def session():
    return Session(teams=[Team(name="GoodTeam", id="secret")])


def test_new_game_can_be_started_with_correct_team_id(session):
    start_game = NewGameUseCase(session=session)
    assert len(session.games) == 0
    start_game(request=NewGameRequest(team_id="secret", n_stones=3))
    assert len(session.games) == 1


def test_new_game_isnt_started_with_unknown_team_id(session):
    start_game = NewGameUseCase(session=session)
    assert len(session.games) == 0
    start_game(request=NewGameRequest(team_id="wrong_id", n_stones=3))
    assert len(session.games) == 0
