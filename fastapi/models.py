from enum import Enum
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Genre(str,Enum):
    K_POP = "k-pop"
    ELECTRONIC = "electronic"
    POP = "pop"

class MusicForm(SQLModel):
    name: str
    artist: str
    genre: Genre

class Music(MusicForm, table=True):
    id: int = Field(default=None, primary_key=True)

class MusicUpdate(BaseModel):
    name: str | None = None
    artist: str | None = None
    genre: Genre | None = None