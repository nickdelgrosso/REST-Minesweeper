from minesweeper.entitites import Team


def test_team_creates_with_unique_string_ids():
    team1 = Team.init(name="Cool Peeps")
    team2 = Team.init(name="Cool Peeps")
    assert isinstance(team1.name, str)
    assert team1.name == team2.name
    assert isinstance(team1.id, str)
    assert team1.id != team2.id

