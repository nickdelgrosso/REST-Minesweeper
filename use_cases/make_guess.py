from typing import Tuple

from pydantic import BaseModel

from use_cases.base import BaseUseCase


class GuessRequest(BaseModel):
    team_id: str
    game_id: str
    guess: Tuple[str]


class GuessResponse(BaseModel):
    num: int
    won: bool
    n_correct: int
    n_incorrect: int
    n_unknown: int


class MakeGuessUseCase(BaseUseCase):

    def __call__(self, request: GuessRequest):
        ...