from typing import List

from fastapi import APIRouter
from pydantic.main import BaseModel

from data import inmemory
from minesweeper.entitites import Team


router = APIRouter()


class PublicTeamResponse(BaseModel):
    name: str

class PublicTeamListResponse(BaseModel):
    teams: List[PublicTeamResponse]

    @classmethod
    def from_teams(cls, teams: List[Team]):
        return cls(
            teams=[PublicTeamResponse(name=team.name) for team in teams],
        )


@router.get("/teams", response_model=PublicTeamListResponse)
async def teams():
    session = inmemory.session
    return PublicTeamListResponse.from_teams(teams=session.teams)