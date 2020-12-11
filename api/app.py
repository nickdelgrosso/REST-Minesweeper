from fastapi import FastAPI

from minesweeper.cases.list_teams import TeamListResponse
from minesweeper.cases.new_game import NewGameResponse, NewGameRequest
from minesweeper.cases.register_team import RegistrationRequest, RegistrationResponse
from minesweeper.cases.reset_session import ResetResponse, ResetRequest
from minesweeper.provider import UseCaseProvider

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Lean Minesweeper!"}


@app.post("/reset", response_model=ResetResponse)
async def reset_session(request: ResetRequest) -> ResetResponse:
    use_cases = UseCaseProvider()
    return use_cases.reset_session(username=request.username, password=request.password)


@app.get("/teams", response_model=TeamListResponse)
async def teams():
    return UseCaseProvider().list_teams()


@app.post("/register", response_model=RegistrationResponse)
async def register(request: RegistrationRequest):
    return UseCaseProvider().register_team(request=request)


@app.post("/new-game", response_model=NewGameResponse)
def register_new_game(request: NewGameRequest):
    return UseCaseProvider().start_new_game(request=request)
