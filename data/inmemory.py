from dataclasses import dataclass, field
from typing import Dict, List
from uuid import uuid4

from minesweeper.entitites import Game, Team


@dataclass
class Session:
    teams: List[Team] = field(default_factory=list)
    games: Dict[str, Game] = field(default_factory=dict)

    @classmethod
    def init(cls):
        return cls()

    def reset(self):
        self.teams = []
        self.games = {}

    def add_team(self, team: Team):
        self.teams.append(team)

    def team_id_exists(self, id: str):
        return any(team.id == id for team in self.teams)

    def add_game(self, game: Game) -> str:
        game_id = str(uuid4())
        self.games[game_id] = game
        return game_id

    def game_id_exists(self, id: str):
        return any(team.id == id for team in self.teams)


session = Session()