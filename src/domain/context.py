from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Team:
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))
