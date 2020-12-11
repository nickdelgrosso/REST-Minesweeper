from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from minesweeper.entitites import Team, Session

app = FastAPI()

session = Session.init()


class Message(BaseModel):
    message: str


@app.get("/", response_model=Message)
async def root():
    return {"message": "Welcome to Lean Minesweeper!"}


class RegistrationRequest(BaseModel):
    team_name: str
    do_registration: bool = False

class RegistrationResponse(BaseModel):
    is_registered: bool
    team_name: str
    team_id: str


@app.post("/register", response_model=RegistrationResponse)
async def register(request: RegistrationRequest):
    team = Team.init(name=request.team_name)
    if request.do_registration:
        session.register_team(team=team)
    response = RegistrationResponse(
        is_registered=request.do_registration,
        team_name=team.name,
        team_id=team.id
    )
    return response


class PublicTeamResponse(BaseModel):
    name: str

class PublicTeamListResponse(BaseModel):
    teams: List[PublicTeamResponse]

    @classmethod
    def from_teams(cls, teams: List[Team]):
        return cls(
            teams=[PublicTeamResponse(name=team.name) for team in teams],
        )


@app.get("/teams", response_model=PublicTeamListResponse)
async def teams():
    return PublicTeamListResponse.from_teams(teams=session.teams)
