import pytest

from domain.entities import Team, Game
from domain.value_objects import Colors, Hint


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
    ((red, red, red, red), (green, green, green, green), 0, 0),
    ((red, red, red, green), (green, green, green, green), 1, 0),
    ((green, red, red, green), (green, green, green, green), 2, 0),
    ((green, red, red, green), (red, red, red, red), 2, 0),
    ((green, red, red, green), (green, red, red, green), 4, 0),
]
@pytest.mark.parametrize("solution, guess, n_correct, n_incorrect", cases)
def test_can_calculate_correct_placements(solution, guess, n_correct, n_incorrect):
    hint = Hint.from_comparison(guess=guess, solution=solution)
    assert hint.correct_placements == n_correct
    assert hint.incorrect_placements == n_incorrect
