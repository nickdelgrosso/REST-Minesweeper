from __future__ import annotations

from collections import Counter
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
    correct: int
    incorrect: int
    unknown: int

    @classmethod
    def from_comparison(cls, guess: Sequence[Colors], solution: Sequence[Colors]) -> Hint:
        if len(guess) != len(solution):
            raise IncorrectNumberOfStonesError(f"Game has {len(solution)} stones, guess had {len(guess)} stones.")

        remaining_guess, remaining_solution = [], []
        correct = 0
        for solution_stone, guess_stone in zip(solution, guess):
            if solution_stone == guess_stone:
                correct += 1
            else:
                remaining_guess.append(guess_stone)
                remaining_solution.append(solution_stone)

        guess_counts = Counter(remaining_guess)
        solution_counts = Counter(remaining_solution)
        incorrect = sum(min(guess_counts[color], solution_counts[color]) for color in Colors)
        unknown = len(guess) - correct - incorrect

        assert (correct + incorrect + unknown) == len(guess), "Total of hints must equal number of stones."
        return cls(
            correct=correct,
            incorrect=incorrect,
            unknown=unknown,
        )
