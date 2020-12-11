from fastapi import FastAPI

from routes import ping, register_team, list_teams, reset_session, new_game

app = FastAPI()
app.include_router(ping.router)
app.include_router(register_team.router)
app.include_router(list_teams.router)
app.include_router(reset_session.router)
app.include_router(new_game.router)

#
# class NewGameRequest(BaseModel):
#     team_id: str
#
# @app.post("/new-game")
# async def new_game(request: NewGameRequest):
#     ...
