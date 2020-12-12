from dataclasses import dataclass, field
from typing import List

from src.domain import Game, Team


@dataclass
class Session:
    teams: List[Team] = field(default_factory=list)
    games: List[Game] = field(default_factory=list)

    def reset(self):
        self.teams = []
        self.games = []

    def add_team(self, team: Team):
        self.teams.append(team)

    def get_team(self, id: str):
        for team in self.teams:
            if team.id == id:
                return team

    def add_game(self, game: Game):
        self.games.append(game)


session = Session()
