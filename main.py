from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from data import inmemory
from minesweeper.entitites import Team, Session
from routes import ping, register

app = FastAPI()
app.include_router(ping.router)
app.include_router(register.router)




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
    session = inmemory.session
    return PublicTeamListResponse.from_teams(teams=session.teams)


class PublicResetRequest(BaseModel):
    username: str
    password: str

class PublicResetResponse(BaseModel):
    successful: bool

@app.post("/reset")
async def reset_session(request: PublicResetRequest):
    if request.username == "nickdg" and request.password == "flipthetable":  # Just for demo, never do this for production code!!!!
        inmemory.session = Session.init()
        return PublicResetResponse(successful=True)
    else:
        return PublicResetResponse(successful=False)

#
# class NewGameRequest(BaseModel):
#     team_id: str
#
# @app.post("/new-game")
# async def new_game(request: NewGameRequest):
#     ...