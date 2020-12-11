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


r, g, b, y = Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW
cases = [
    ((r, r, r, r), (g, g, g, g), 0, 0, 4),
    ((r, r, r, g), (g, g, g, g), 1, 0, 3),
    ((g, r, r, g), (g, g, g, g), 2, 0, 2),
    ((g, r, r, g), (r, r, r, r), 2, 0, 2),
    ((g, r, r, g), (g, r, r, g), 4, 0, 0),
    ((r, r, r, g), (g, b, b, b), 0, 1, 3),
    ((r, r, g, g), (g, g, b, b), 0, 2, 2),
    ((r, g, g, g), (g, b, b, b), 0, 1, 3),
    ((b, g, g, g), (g, b, b, b), 0, 2, 2),
    ((r, g, b, b), (b, b, r, g), 0, 4, 0),
    ((r, g), (g, r), 0, 2, 0),
    ((r, r), (r, r), 2, 0, 0),
    ((r, g, b), (r, b, y), 1, 1, 1),
    ((y, b, g, r, y, b, y, g, b), (b, g, y, b, r, r, g, r, b), 1, 6, 2),
    ((y, r, r, r, g, b, r, y, y), (b, g, y, r, y, y, r, r, g), 2, 6, 1),
]


@pytest.mark.parametrize("solution, guess, correct, incorrect, unknown", cases)
def test_game_can_tell_correct_placements(solution, guess, correct, incorrect, unknown):
    game = Game(solution=solution)
    hint = game.guess(guess)
    assert hint.correct == correct
    assert hint.incorrect == incorrect
    assert hint.unknown == unknown
