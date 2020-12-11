from fastapi import FastAPI

from api.routes import register_team, new_game
from minesweeper.cases.list_teams import PublicTeamListResponse
from minesweeper.cases.register_team import RegistrationRequest, RegistrationResponse
from minesweeper.cases.reset_session import ResetResponse, ResetRequest
from minesweeper.use_cases import UseCaseProvider

app = FastAPI()
app.include_router(register_team.router)
app.include_router(new_game.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Lean Minesweeper!"}


@app.post("/reset", response_model=ResetResponse)
async def reset_session(request: ResetRequest) -> ResetResponse:
    use_cases = UseCaseProvider()
    return use_cases.reset_session(request=request)


@app.get("/teams", response_model=PublicTeamListResponse)
async def teams():
    return UseCaseProvider().list_teams()


@app.post("/register", response_model=RegistrationResponse)
async def register(request: RegistrationRequest):
    return UseCaseProvider().register_team(request=request)
