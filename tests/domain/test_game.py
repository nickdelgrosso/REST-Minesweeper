from src.domain import Team


def test_team_gets_a_unique_id_upon_generation():
    t1 = Team("A")
    assert t1.id
    t2 = Team("B")
    assert t2.id
    assert t1.id != t2.id
