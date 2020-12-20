import pytest

from src.domain import Team, Puzzle, Colors


def test_team_creates_with_unique_string_ids():
    team1 = Team(name="Cool Peeps")
    team2 = Team(name="Cool Peeps")
    assert isinstance(team1.name, str)
    assert team1.name == team2.name
    assert isinstance(team1.id, str)
    assert team1.id != team2.id


def test_puzzle_knows_how_many_stones_it_has():
    puzzle = Puzzle.init(n_stones=4)
    assert puzzle.n_stones == 4
    puzzle = Puzzle.init(n_stones=2)
    assert puzzle.n_stones == 2

    puzzle = Puzzle(solution=(Colors.RED, Colors.RED, Colors.RED))
    assert puzzle.n_stones == 3

    puzzle = Puzzle(solution=(Colors.BLUE, Colors.GREEN, Colors.RED, Colors.RED))
    assert puzzle.n_stones == 4


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
def test_puzzle_can_tell_correct_placements(solution, guess, correct, incorrect, unknown):
    hint = Puzzle.get_clue(solution=solution, guess=guess)
    assert hint.correct == correct
    assert hint.incorrect == incorrect
    assert hint.unknown == unknown


def test_empty_game_has_no_last_clue():
    puzzle = Puzzle(solution=(r, r, r))
    assert puzzle.last_clue is None


def test_guessing_updates_turn_counter():
    puzzle = Puzzle(solution=(r, r, r))
    for idx in range(10):
        puzzle = puzzle.guess((r, r, g))
        assert puzzle.num_turns == idx + 1


def test_guessing_correctly_activates_win_flag():
    puzzle = Puzzle(solution=(r, r, r))
    assert puzzle.won is False
    puzzle = puzzle.guess((g, g, g))
    assert puzzle.won is False
    puzzle = puzzle.guess((r, r, g))
    assert puzzle.won is False
    puzzle = puzzle.guess((r, r, r))
    assert puzzle.won is True
    puzzle = puzzle.guess((r, b, b))
    assert puzzle.won is True