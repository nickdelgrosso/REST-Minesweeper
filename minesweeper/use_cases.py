from pydantic.main import BaseModel

from data.inmemory import session


class ResetRequest(BaseModel):
    username: str
    password: str


class ResetResponse(BaseModel):
    successful: bool


class UseCaseProvider:
    def __init__(self):
        self.session = session

    def reset_session(self, request: ResetRequest) -> ResetResponse:
        if request.username == "nickdg" and request.password == "flipthetable":  # Just for demo, never do this for production code!!!!
            self.session.reset()
            return ResetResponse(successful=True)
        else:
            return ResetResponse(successful=False)
