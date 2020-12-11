from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from data import inmemory
from minesweeper.entitites import Team, Session
from routes import ping, register, list_teams

app = FastAPI()
app.include_router(ping.router)
app.include_router(register.router)
app.include_router(list_teams.router)


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