def chelsea_player_schema(chelsea_player) -> dict:
    """
    Helper function that converts a chelsea player object into a dictionary schema.

    Args:
        chelsea_player (dict): A dictionary representing a chelsea player object.

    Returns:
        dict: A dictionary containing selected fields from the chelsea player object.
            The dictionary schema includes the following keys:
            - 'name': The name of the player.
            - 'nationality': The nationality of the player.
            - 'position': The position that the player used to play on the pitch.
            - 'career': The carrer time frame when the user played for chelsea.
            - 'goals': The cuantity of goals that the player score for the team.
            - 'appearances': The total appearances that the player got for chelsea.

    """
    return {"name": chelsea_player["name"],
            "nationality": chelsea_player["nationality"],
            "position": chelsea_player["position"],
            "career": chelsea_player["career"],
            "goals": chelsea_player["goals"],
            "appearances": chelsea_player["appearances"]}


def chelsea_players_schema(chelsea_players) -> list:
    """
    Helper function that converts a list of chelsea player objects into a list of dictionary schemas.

    Args:
        chelsea_players (list): A list of chelsea players objects, where each object is a dictionary.

    Returns:
        list: A list of dictionary schemas, where each dictionary represents a chelsea player.

    """
    return [chelsea_player_schema(chelsea_player) for chelsea_player in chelsea_players]