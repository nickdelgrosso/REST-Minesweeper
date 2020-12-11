from pydantic.main import BaseModel

from minesweeper.cases.base import BaseUseCase
from minesweeper.entitites import Team


class RegistrationRequest(BaseModel):
    team_name: str


class RegistrationResponse(BaseModel):
    team_id: str


class RegisterTeamUseCase(BaseUseCase):

    def __call__(self, request: RegistrationRequest) -> RegistrationResponse:
        team = Team(name=request.team_name)
        self.session.add_team(team=team)
        return RegistrationResponse(
            team_id=team.id
        )
