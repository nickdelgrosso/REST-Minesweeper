from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple
from uuid import uuid4


@dataclass
class Team:
    name: str
    id: str

    @classmethod
    def init(cls, name: str):
        return cls(name=name, id=str(uuid4()))

class Colors(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'
    ORANGE = 'orange'


@dataclass
class Game:
    solution: List[Colors]
    guesses: List[Tuple[Guess, Hint]] = field(default_factory=list)

    @property
    def n_stones(self) -> int:
        return len(self.solution)

    @classmethod
    def init(self, n_stones: int = 4):
        return Game(
            solution=random.choices(list(Colors), k=n_stones),
            guesses=[],
        )


Guess = List[Colors]

@dataclass
class Hint:
    n_correct_placement: int
    n_incorrect_placement: int
    n_unknown: int


@dataclass
class Session:
    games: List[Game]
    teams: List[Team]

    @classmethod
    def init(cls):
        return cls(games=[], teams=[])

    def register_team(self, team: Team):
        self.teams.append(team)

