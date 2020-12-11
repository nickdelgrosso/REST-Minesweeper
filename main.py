from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Message(BaseModel):
    message: str

@app.get("/", response_model=Message)
async def root():
    return {"message": "Welcome to Lean Minesweeper!"}


class RegistrationResponse(BaseModel):
    registered: bool
    team_name: str
    team_id: str

@app.get("/register")
async  def register(team_name: str):
    return {"message": "registered"}