from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field
from typing import Tuple
from uuid import uuid4

from domain.errors import IncorrectNumberOfStonesError
from domain.value_objects import Colors, StoneSequence, Hint


@dataclass(frozen=True)
class Team:
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class Game:
    solution: Tuple[Colors, ...]
    id: str = field(default_factory=lambda: str(uuid4()))

    @property
    def n_stones(self) -> int:
        return len(self.solution)

    @classmethod
    def init(cls, n_stones: int = 4):
        return cls(
            solution=tuple(random.choices(list(Colors), k=n_stones)),
        )

    @staticmethod
    def get_hint(guess: StoneSequence, solution: StoneSequence) -> Hint:
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
        return Hint(
            correct=correct,
            incorrect=incorrect,
            unknown=unknown,
        )

    def guess(self, guess: StoneSequence) -> Hint:
        return self.get_hint(guess=guess, solution=self.solution)
