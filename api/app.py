from fastapi import FastAPI

from api.routes import ping, register_team, new_game
from minesweeper.cases.list_teams import PublicTeamListResponse
from minesweeper.cases.reset_session import ResetResponse, ResetRequest
from minesweeper.use_cases import UseCaseProvider

app = FastAPI()
app.include_router(ping.router)
app.include_router(register_team.router)
app.include_router(new_game.router)


@app.post("/reset", response_model=ResetResponse)
async def reset_session(request: ResetRequest) -> ResetResponse:
    use_cases = UseCaseProvider()
    return use_cases.reset_session(request=request)


@app.get("/teams", response_model=PublicTeamListResponse)
async def teams():
    return UseCaseProvider().list_teams()
