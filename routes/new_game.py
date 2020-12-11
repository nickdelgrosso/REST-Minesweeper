from typing import Optional

from fastapi import APIRouter
from pydantic.main import BaseModel

from data import inmemory
from minesweeper.entitites import Game

router = APIRouter()


class NewGameRequest(BaseModel):
    team_id: str
    n_stones: int


class NewGameResponse(BaseModel):
    successful: bool
    game_id: Optional[str] = None


@router.post("/new-game", response_model=NewGameResponse)
def register_new_game(request: NewGameRequest):
    session = inmemory.session
    if session.team_id_exists(id=request.team_id):
        game = Game.init(n_stones=request.n_stones)
        game_id = session.register_game(game)
        return NewGameResponse(
            successful=True,
            game_id=game_id
        )
    else:
        return NewGameResponse(
            successful=False
        )
