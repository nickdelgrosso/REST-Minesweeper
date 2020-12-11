from dataclasses import dataclass
from enum import Enum
from typing import List


class Colors(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'
    ORANGE = 'orange'


Guess = List[Colors]


@dataclass
class Hint:
    n_correct_placement: int
    n_incorrect_placement: int
    n_unknown: int