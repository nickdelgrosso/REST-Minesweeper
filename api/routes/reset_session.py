from fastapi import APIRouter

from minesweeper.use_cases import ResetRequest, ResetResponse, UseCaseProvider

router = APIRouter()


@router.post("/reset", response_model=ResetResponse)
async def reset_session(request: ResetRequest) -> ResetResponse:
    use_cases = UseCaseProvider()
    return use_cases.reset_session(request=request)
