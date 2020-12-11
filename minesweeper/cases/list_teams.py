from typing import List

from pydantic.main import BaseModel

from minesweeper.cases.base import BaseUseCase
from minesweeper.entitites import Team


class PublicTeamResponse(BaseModel):
    name: str


class PublicTeamListResponse(BaseModel):
    teams: List[PublicTeamResponse]

    @classmethod
    def from_teams(cls, teams: List[Team]):
        return cls(
            teams=[PublicTeamResponse(name=team.name) for team in teams],
        )


class ListTeamsUseCase(BaseUseCase):

    def __call__(self) -> PublicTeamListResponse:
        return PublicTeamListResponse.from_teams(teams=self.session.teams)
