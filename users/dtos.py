from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class AuthResponseDTO:
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str
    accessToken: Optional[str] = None
    refreshToken: Optional[str] = None


@dataclass
class UserDTO:
    id: int
    username: str
    email: str
    firstName: str
    lastName: str

    def to_json(self):
        return asdict(self)
