from dataclasses import dataclass, field
from typing import List

from minesweeper.entitites import Game, Team


@dataclass
class Session:
    teams: List[Team] = field(default_factory=list)
    games: List[Game] = field(default_factory=list)

    @classmethod
    def init(cls):
        return cls()

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

    def game_id_exists(self, id: str):
        return any(game.id == id for game in self.games)


session = Session()
