import pytest

from src.domain.value_objects import Colors, Clue

r, g, b = Colors.RED, Colors.GREEN, Colors.BLUE

cases = [
    (Clue(stones=(r, r, r), correct=3, incorrect=0, unknown=0), True),
    (Clue(stones=(r, r, r), correct=2, incorrect=1, unknown=0), False),
    (Clue(stones=(r, r, r), correct=1, incorrect=2, unknown=0), False),
    (Clue(stones=(r, r, r), correct=0, incorrect=1, unknown=2), False),
    (Clue(stones=(r, r), correct=2, incorrect=0, unknown=0), True),
]
@pytest.mark.parametrize("clue,is_perfect", cases)
def test_clue_can_tell_if_perfect_match(clue, is_perfect):
    assert clue.is_perfect_match is is_perfect