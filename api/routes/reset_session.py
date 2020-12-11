from fastapi import APIRouter

from minesweeper.cases.reset_session import ResetResponse, ResetRequest
from minesweeper.use_cases import UseCaseProvider

router = APIRouter()


@router.post("/reset", response_model=ResetResponse)
async def reset_session(request: ResetRequest) -> ResetResponse:
    use_cases = UseCaseProvider()
    return use_cases.reset_session(request=request)
