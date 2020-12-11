from data.inmemory import session
from use_cases.list_teams import ListTeamsUseCase
from use_cases.new_game import NewGameUseCase
from use_cases.register_team import RegisterTeamUseCase
from use_cases.reset_session import ResetSessionUseCase, ResetRequest, ResetResponse


class UseCaseProvider:
    def __init__(self):
        self.session = session

    def reset_session(self, username: str, password: str) -> ResetResponse:
        return ResetSessionUseCase(session=self.session)(
            request=ResetRequest(
                username=username,
                password=password,
            )
        )

    @property
    def list_teams(self) -> ListTeamsUseCase:
        return ListTeamsUseCase(session=self.session)

    @property
    def register_team(self) -> RegisterTeamUseCase:
        return RegisterTeamUseCase(session=self.session)

    @property
    def start_new_game(self) -> NewGameUseCase:
        return NewGameUseCase(session=self.session)
