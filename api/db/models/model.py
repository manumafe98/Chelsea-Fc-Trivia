from pydantic import BaseModel

class ChelseaPlayers(BaseModel):
    name: str
    nationality: str
    position: str
    career: str
    goals: int
    appearances: int

