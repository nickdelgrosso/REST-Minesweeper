from data.inmemory import Session
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


def test_session_knows_if_team_id_exists():
    team = Team(name='hi', id='abcde')
    session = Session(teams=[team], games=[])
    assert session.get_team(id='abcde') == team
    assert session.get_team(id='aaaaa') is None
