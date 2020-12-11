import pytest

from domain.entities import Team, Game
from domain.value_objects import Colors


def test_team_creates_with_unique_string_ids():
    team1 = Team(name="Cool Peeps")
    team2 = Team(name="Cool Peeps")
    assert isinstance(team1.name, str)
    assert team1.name == team2.name
    assert isinstance(team1.id, str)
    assert team1.id != team2.id


def test_game_knows_how_many_stones_it_has():
    game = Game.init(n_stones=4)
    assert game.n_stones == 4
    game = Game.init(n_stones=2)
    assert game.n_stones == 2

    game = Game(solution=(Colors.RED, Colors.RED, Colors.RED))
    assert game.n_stones == 3

    game = Game(solution=(Colors.BLUE, Colors.GREEN, Colors.RED, Colors.RED))
    assert game.n_stones == 4


red, green = Colors.RED, Colors.GREEN
cases = [
    ((red, red, red, red), (green, green, green, green), 0),
]
@pytest.mark.parametrize("solution, guess, n_correct", cases)
def test_game_can_tell_correct_placements(solution, guess, n_correct):
    game = Game(solution=solution)
    hint = game.guess(guess)
    assert hint.n_correct_placement == n_correct
