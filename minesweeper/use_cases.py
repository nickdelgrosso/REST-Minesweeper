from data.inmemory import session
from minesweeper.cases.list_teams import ListTeamsUseCase
from minesweeper.cases.register_team import RegisterTeamUseCase
from minesweeper.cases.reset_session import ResetSessionUseCase


class UseCaseProvider:
    def __init__(self):
        self.session = session

    @property
    def reset_session(self) -> ResetSessionUseCase:
        return ResetSessionUseCase(session=self.session)

    @property
    def list_teams(self) -> ListTeamsUseCase:
        return ListTeamsUseCase(session=self.session)

    @property
    def register_team(self) -> RegisterTeamUseCase:
        return RegisterTeamUseCase(session=self.session)
