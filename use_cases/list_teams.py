from typing import List

from pydantic.main import BaseModel

from use_cases.base import BaseUseCase
from domain.entities import Team


class TeamResponse(BaseModel):
    name: str


class TeamListResponse(BaseModel):
    teams: List[TeamResponse]

    @classmethod
    def from_teams(cls, teams: List[Team]):
        return cls(
            teams=[TeamResponse(name=team.name) for team in teams],
        )


class ListTeamsUseCase(BaseUseCase):

    def __call__(self) -> TeamListResponse:
        return TeamListResponse.from_teams(teams=self.session.teams)
