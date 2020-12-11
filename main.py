from fastapi import FastAPI

from routes import ping, register, list_teams, reset_session

app = FastAPI()
app.include_router(ping.router)
app.include_router(register.router)
app.include_router(list_teams.router)
app.include_router(reset_session.router)

#
# class NewGameRequest(BaseModel):
#     team_id: str
#
# @app.post("/new-game")
# async def new_game(request: NewGameRequest):
#     ...
