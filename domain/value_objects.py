from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Sequence

from domain.errors import IncorrectNumberOfStonesError


class Colors(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'
    ORANGE = 'orange'


Guess = List[Colors]


@dataclass(frozen=True)
class Hint:
    correct_placements: int
    incorrect_placements: int
    n_unknown: int

    @classmethod
    def from_comparison(cls, guess: Sequence[Colors], solution: Sequence[Colors]) -> Hint:
        if len(guess) != len(solution):
            raise IncorrectNumberOfStonesError(f"Game has {len(solution)} stones, guess had {len(guess)} stones.")

        correct_placements = 0
        for solution_stone, guess_stone in zip(solution, guess):
            if solution_stone == guess_stone:
                correct_placements += 1
        return cls(
            correct_placements=correct_placements,
            incorrect_placements=0,
            n_unknown=0,
        )
