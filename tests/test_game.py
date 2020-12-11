from minesweeper.entitites import Team, Game, Colors, Guess


def test_team_creates_with_unique_string_ids():
    team1 = Team.init(name="Cool Peeps")
    team2 = Team.init(name="Cool Peeps")
    assert isinstance(team1.name, str)
    assert team1.name == team2.name
    assert isinstance(team1.id, str)
    assert team1.id != team2.id


def test_game_knows_how_many_stones_it_has():
    game = Game.init(n_stones=4)
    assert game.n_stones == 4
    game = Game.init(n_stones=2)
    assert game.n_stones == 2

    game = Game(solution=[Colors.RED, Colors.RED, Colors.RED])
    assert game.n_stones == 3

    game = Game(solution=[Colors.BLUE, Colors.GREEN, Colors.RED, Colors.RED])
    assert game.n_stones == 4