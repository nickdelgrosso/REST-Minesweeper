from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from typing import Tuple, Optional
from uuid import uuid4


@dataclass(frozen=True)
class Team:
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass(frozen=True)
class Puzzle:
    solution: StoneSequence
    clues: Tuple[Clue, ...] = field(default_factory=tuple)
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
    def get_clue(guess: StoneSequence, solution: StoneSequence) -> Clue:
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
        return Clue(
            stones=guess,
            correct=correct,
            incorrect=incorrect,
            unknown=unknown,
        )

    @property
    def num_turns(self) -> int:
        return len(self.clues)

    @property
    def last_clue(self) -> Optional[Clue]:
        return self.clues[-1] if self.clues else None

    @property
    def won(self) -> bool:
        return any(clue.is_perfect_match for clue in self.clues[::-1])

    def guess(self, guess: StoneSequence) -> Puzzle:
        clue = self.get_clue(guess=guess, solution=self.solution)
        return Puzzle(
            solution=self.solution,
            clues=self.clues + (clue,),
            id=self.id,
        )


class IncorrectNumberOfStonesError(Exception):
    ...


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