from fastapi import FastAPI

from api.routes import ping, register_team, list_teams, reset_session, new_game

app = FastAPI()
app.include_router(ping.router)
app.include_router(register_team.router)
app.include_router(list_teams.router)
app.include_router(reset_session.router)
app.include_router(new_game.router)
