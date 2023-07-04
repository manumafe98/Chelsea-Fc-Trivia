def chelsea_player_schema(chelsea_player) -> dict:
    return {"name": chelsea_player["name"],
            "nationality": chelsea_player["nationality"],
            "position": chelsea_player["position"],
            "career": chelsea_player["career"],
            "goals": chelsea_player["goals"],
            "appearances": chelsea_player["appearances"]}


def chelsea_players_schema(chelsea_players) -> list:
    return [chelsea_player_schema(chelsea_player) for chelsea_player in chelsea_players]