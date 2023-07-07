from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from db.client import db_client
from db.models.model import ChelseaPlayer
from db.schemas.schemas import chelsea_players_schema, chelsea_player_schema


router = APIRouter()


@router.get("/")
async def home():
    """
    Routes the user from the / to the /docs.

    Returns:
        RedirectResponse: A redirect response to the /docs page.
    """
    return RedirectResponse("/docs", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/players", response_model=list[ChelseaPlayer], status_code=status.HTTP_200_OK)
async def players():
    """
    Gets 3 random records from the mongodb database and returns a list.

    Returns:
        list[ChelseaPlayer]: A list of chelsea players.
    """
    # How many goals did: PLAYER score?
    random_players = db_client.chelsea_players.aggregate([{"$sample": {"size": 3}}])
    return chelsea_players_schema(random_players)
    

@router.get("/nationality", status_code=status.HTTP_200_OK)
async def nationality_question():
    """
    Gets a random record from the database, 
    and then two other random records that have different nationality from the first one.

    Returns:
        A dictionary containing the following information:
        - "nationality": The nationality of first randomized player.
        - "correct_answer": The name of the player that is the correct answer.
        - "players": An array of player objects.
    """
    # Which player of the followings is from: COUNTRY?
    random_data = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player = chelsea_players_schema(random_data)[0]
    nationality = random_player["nationality"]
    random_players = db_client.chelsea_players.aggregate([{"$match": {"nationality": {"$ne": nationality}}}, 
                                                          {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(random_player)
    return {"nationality": nationality, "corect_answer": random_player["name"], "players": players_array}


@router.get("/position", status_code=status.HTTP_200_OK)
async def position_question():
    """
    Gets a random record from the database, 
    and then two other random records that have different positions from the first one.

    Returns:
        A dictionary containing the following information:
        - "position": The position of first randomized player.
        - "correct_answer": The name of the player that is the correct answer.
        - "players": An array of player objects.
    """
    # Which one of the following players used to play as: POSITION?
    random_data = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player = chelsea_players_schema(random_data)[0]
    position = random_player["position"]
    random_players = db_client.chelsea_players.aggregate([{"$match": {"position": {"$ne": position}}}, 
                                                          {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(random_player)
    return {"position": position, "corect_answer": random_player["name"], "players": players_array}


@router.get("/top_appearances", status_code=status.HTTP_200_OK)
async def top_appearances():
    """
    Gets the record with most appearances in the database and then two other random players.

    Returns:
        A dictionary containing the following information:
        - "correct_answer": The name of the player that has the most appearances.
        - "players": An array of player objects.
    """
    # Which one of these players has the most appearances for chelsea?
    sort_criteria = [("appearances", -1)]
    player_with_most_appearances = chelsea_player_schema(db_client.chelsea_players.find_one(sort=sort_criteria))
    player_with_most_appearances_name = player_with_most_appearances["name"]
    random_players = db_client.chelsea_players.aggregate([
        {"$match": {"name": {"$ne": player_with_most_appearances_name}}}, {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(player_with_most_appearances)
    return {"corect_answer": player_with_most_appearances_name, "players": players_array}


@router.get("/top_goalscorer", status_code=status.HTTP_200_OK)
async def top_goalscorer():
    """
    Gets the record with most goals in the database and then two other random players.

    Returns:
        A dictionary containing the following information:
        - "correct_answer": The name of the player that has the most goals.
        - "players": An array of player objects.
    """
    # Which one of these players is the top goalscorer of chelsea?
    sort_criteria = [("goals", -1)]
    player_with_most_goals = chelsea_player_schema(db_client.chelsea_players.find_one(sort=sort_criteria))
    player_with_most_goals_name = player_with_most_goals["name"]
    random_players = db_client.chelsea_players.aggregate([
        {"$match": {"name": {"$ne": player_with_most_goals_name}}}, {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(player_with_most_goals)
    return {"corect_answer": player_with_most_goals_name, "players": players_array}


@router.get("/most_goals", status_code=status.HTTP_200_OK)
async def most_goals():
    """
    Gets 3 random players with differents amounts of goals, and calculates which one of those 3 has the most goals.

    Returns:
        A dictionary containing the following information:
        - "goals": The amount of goals of the one with most.
        - "correct_answer": The name of the player that has the most goals.
        - "players": An array of player objects.
    """
    # Which player of the following have the most goals?
    random_data1 = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player1 = chelsea_players_schema(random_data1)[0]

    random_data2 = db_client.chelsea_players.aggregate([{"$match": {"goals": {"$ne": random_player1["goals"]}}}, 
                                                        {"$sample": {"size": 1}}])
    random_player2 = chelsea_players_schema(random_data2)[0]

    random_data3 = db_client.chelsea_players.aggregate([{"$match": 
                                                         {"$and": [{"goals": {"$ne": random_player1["goals"]}}, 
                                                                   {"goals": {"$ne": random_player2["goals"]}}]}},
                                                                   {"$sample": {"size": 1}}])
    random_player3 = chelsea_players_schema(random_data3)[0]
    player_array = [random_player1, random_player2, random_player3]
    goals = 0
    name = ""
    for player in player_array:
        if player["goals"] >= goals:
            goals = player["goals"]
            name = player["name"]
    return {"goals": goals, "correct_answer": name, "players": player_array}


@router.get("/most_appearances", status_code=status.HTTP_200_OK)
async def most_appearances():
    """
    Gets 3 random players with differents amounts of appearances, 
    and calculates which one of those 3 has the most appearances.

    Returns:
        A dictionary containing the following information:
        - "appearances": The amount of appearances of the one with most.
        - "correct_answer": The name of the player that has the most appearances.
        - "players": An array of player objects.
    """
    # Which player of the following have the most appereances?
    random_data1 = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player1 = chelsea_players_schema(random_data1)[0]

    random_data2 = db_client.chelsea_players.aggregate([{"$match": {"appearances": 
                                                                    {"$ne": random_player1["appearances"]}}}, 
                                                                    {"$sample": {"size": 1}}])
    random_player2 = chelsea_players_schema(random_data2)[0]

    random_data3 = db_client.chelsea_players.aggregate([{"$match": 
                                                         {"$and": 
                                                          [{"appearances": {"$ne": random_player1["appearances"]}}, 
                                                           {"appearances": {"$ne": random_player2["appearances"]}}]}}, 
                                                           {"$sample": {"size": 1}}])
    random_player3 = chelsea_players_schema(random_data3)[0]
    player_array = [random_player1, random_player2, random_player3]
    appearances = 0
    name = ""
    for player in player_array:
        if player["appearances"] >= appearances:
            appearances = player["appearances"]
            name = player["name"]
    return {"appearances": appearances, "correct_answer": name, "players": player_array}


# TODO add content to readme
# TODO start building the frontend that consumes the api
