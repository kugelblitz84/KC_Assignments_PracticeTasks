from dataclasses import dataclass, field
from typing import Any


@dataclass
class response_dto:
    success: bool
    message: str = ""
    data: dict[str, Any] = field(default_factory=dict)


@dataclass
class User:
    username: str
    password_hash: str
    email: str = ""
    token: str = ""


@dataclass
class Session:
    username: str = ""
    token: str = ""

    def clear(self):
        self.username = ""
        self.token = ""


current_session = Session()
