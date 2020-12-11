from fastapi import APIRouter
from pydantic.main import BaseModel

from data.inmemory import session

router = APIRouter()

class PublicResetRequest(BaseModel):
    username: str
    password: str


class PublicResetResponse(BaseModel):
    successful: bool


@router.post("/reset")
async def reset_session(request: PublicResetRequest):
    if request.username == "nickdg" and request.password == "flipthetable":  # Just for demo, never do this for production code!!!!
        session.reset()
        return PublicResetResponse(successful=True)
    else:
        return PublicResetResponse(successful=False)
