from pydantic.main import BaseModel

from use_cases.base import BaseUseCase


class ResetRequest(BaseModel):
    username: str
    password: str


class ResetResponse(BaseModel):
    successful: bool


class ResetSessionUseCase(BaseUseCase):

    def __call__(self, request: ResetRequest) -> ResetResponse:
        if request.username == "nickdg" and request.password == "flipthetable":  # Just for demo, never do this for production code!!!!
            self.session.reset()
            return ResetResponse(successful=True)
        else:
            return ResetResponse(successful=False)