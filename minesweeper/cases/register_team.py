from pydantic.main import BaseModel

from minesweeper.cases.base import BaseUseCase
from minesweeper.entitites import Team


class RegistrationRequest(BaseModel):
    team_name: str
    do_registration: bool = False


class RegistrationResponse(BaseModel):
    is_registered: bool
    team_name: str
    team_id: str


class RegisterTeamUseCase(BaseUseCase):

    def __call__(self, request: RegistrationRequest) -> RegistrationResponse:
        team = Team(name=request.team_name)
        if request.do_registration:
            self.session.add_team(team=team)
        return RegistrationResponse(
            is_registered=request.do_registration,
            team_name=team.name,
            team_id=team.id
        )
