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


class InvalidClueError(Exception):
    ...


@dataclass(frozen=True)
class Clue:
    stones: StoneSequence
    correct: int
    incorrect: int
    unknown: int

    def __post_init__(self):
        self.validate()

    def validate(self):
        if len(self.stones) != self.correct + self.incorrect + self.unknown:
            raise InvalidClueError(str(self))

    @property
    def is_perfect_match(self) -> bool:
        return self.correct == len(self.stones)
