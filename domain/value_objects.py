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
    n_correct_placement: int
    n_incorrect_placement: int
    n_unknown: int

    @classmethod
    def compare(cls, guess: Sequence[Colors], solution: Sequence[Colors]):
        if len(guess) != len(solution):
            raise IncorrectNumberOfStonesError(f"Game has {len(solution)} stones, guess had {len(guess)} stones.")

        correct_placements = 0
        for solution_stone, guess_stone in zip(solution, guess):
            if solution_stone == guess_stone:
                correct_placements += 1
        return cls(
            n_correct_placement=correct_placements,
            n_incorrect_placement=0,
            n_unknown=0,
        )
