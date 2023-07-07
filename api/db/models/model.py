from pydantic import BaseModel

class ChelseaPlayer(BaseModel):
    """A Pydantic model representing a Chelsea Player.

    Attributes:
        name (str): The name of the Chelsea Player.
        nationality (str): The nationality of the Chelsea Player.
        position (str): The position that the player used to play on the pitch.
        career (str): The carrer time frame when the user played for chelsea.
        goals (int): The cuantity of goals that the player score for the team.
        appearances (int): The total appearances that the player got for chelsea.
    """
    name: str
    nationality: str
    position: str
    career: str
    goals: int
    appearances: int
