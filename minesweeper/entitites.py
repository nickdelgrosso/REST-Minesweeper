from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Tuple
from uuid import uuid4

from minesweeper.value_objects import Colors


@dataclass(frozen=True)
class Team:
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class Game:
    solution: Tuple[Colors, ...]
    guesses: List[Tuple[Guess, Hint]] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid4()))

    @property
    def n_stones(self) -> int:
        return len(self.solution)

    @classmethod
    def init(cls, n_stones: int = 4):
        return cls(
            solution=tuple(random.choices(list(Colors), k=n_stones)),
        )


Guess = List[Colors]


@dataclass
class Hint:
    n_correct_placement: int
    n_incorrect_placement: int
    n_unknown: int
