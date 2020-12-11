from fastapi import APIRouter
from pydantic.main import BaseModel

router = APIRouter()


class Message(BaseModel):
    message: str


@router.get("/", response_model=Message)
async def root():
    return {"message": "Welcome to Lean Minesweeper!"}
