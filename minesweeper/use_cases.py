from data.inmemory import session
from minesweeper.cases.reset_session import ResetSessionUseCase


class UseCaseProvider:
    def __init__(self):
        self.session = session

    @property
    def reset_session(self) -> ResetSessionUseCase:
        return ResetSessionUseCase(session=self.session)
