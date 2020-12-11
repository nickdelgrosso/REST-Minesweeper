from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Colors(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'
    ORANGE = 'orange'


StoneSequence = Tuple[Colors, ...]


@dataclass(frozen=True)
class Hint:
    correct: int
    incorrect: int
    unknown: int
