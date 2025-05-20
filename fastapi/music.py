from enum import Enum
from pydantic import BaseModel, Field

class Genre(str,Enum):
    K_POP = "k-pop"
    ELECTRONIC = "electronic"
    POP = "pop"

class MusicForm(BaseModel):
    name: str
    artist: str
    genre: Genre

class Music(MusicForm):
    id: int = 0
