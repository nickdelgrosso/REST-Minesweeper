from fastapi import FastAPI
from pydantic import BaseModel

from minesweeper.entitites import Team

app = FastAPI()


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
    response = RegistrationResponse(
        is_registered=request.do_registration,
        team_name=team.name,
        team_id=team.id
    )
    return response
