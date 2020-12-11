from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Tuple
from uuid import uuid4

from domain.errors import IncorrectNumberOfStonesError
from domain.value_objects import Colors, Guess, Hint


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

    def guess(self, guess: Guess) -> Hint:
        return Hint.compare(guess=guess, solution=self.solution)
