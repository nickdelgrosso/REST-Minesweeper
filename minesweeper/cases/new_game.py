from typing import Optional

from pydantic.main import BaseModel

from data import inmemory
from minesweeper.cases.base import BaseUseCase
from minesweeper.entitites import Game


class NewGameRequest(BaseModel):
    team_id: str
    n_stones: int


class NewGameResponse(BaseModel):
    successful: bool
    game_id: Optional[str] = None


class NewGameUseCase(BaseUseCase):

    def __call__(self, request: NewGameRequest):
        session = inmemory.session
        if session.team_id_exists(id=request.team_id):
            game = Game.init(n_stones=request.n_stones)
            session.add_game(game)
            return NewGameResponse(
                successful=True,
                game_id=game.id
            )
        else:
            return NewGameResponse(
                successful=False
            )
