from fastapi import APIRouter
from pydantic.main import BaseModel

from data.inmemory import session
from minesweeper.entitites import Team

router = APIRouter()


class RegistrationRequest(BaseModel):
    team_name: str
    do_registration: bool = False


class RegistrationResponse(BaseModel):
    is_registered: bool
    team_name: str
    team_id: str


@router.post("/register", response_model=RegistrationResponse)
async def register(request: RegistrationRequest):
    team = Team.init(name=request.team_name)
    if request.do_registration:
        session.register_team(team=team)
        print(session)
    response = RegistrationResponse(
        is_registered=request.do_registration,
        team_name=team.name,
        team_id=team.id
    )
    return response
