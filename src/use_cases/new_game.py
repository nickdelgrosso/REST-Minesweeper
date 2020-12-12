from typing import Optional

from pydantic.main import BaseModel

from src.domain import Game
from src.use_cases.base import BaseUseCase


class NewGameRequest(BaseModel):
    team_id: str
    n_stones: int


class NewGameResponse(BaseModel):
    game_id: Optional[str] = None


class NewGameUseCase(BaseUseCase):

    def __call__(self, request: NewGameRequest):
        session = self.session
        if session.get_team(id=request.team_id):
            game = Game.init(n_stones=request.n_stones)
            session.add_game(game)
            return NewGameResponse(
                game_id=game.id
            )
