from fastapi import FastAPI

from api.routes import ping, register_team, list_teams, new_game
from minesweeper.cases.reset_session import ResetResponse, ResetRequest
from minesweeper.use_cases import UseCaseProvider

app = FastAPI()
app.include_router(ping.router)
app.include_router(register_team.router)
app.include_router(list_teams.router)
app.include_router(new_game.router)


@app.post("/reset", response_model=ResetResponse)
async def reset_session(request: ResetRequest) -> ResetResponse:
    use_cases = UseCaseProvider()
    return use_cases.reset_session(request=request)
