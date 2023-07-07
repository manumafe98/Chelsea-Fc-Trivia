from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from db.client import db_client
from db.models.model import ChelseaPlayers
from db.schemas.schemas import chelsea_players_schema, chelsea_player_schema


router = APIRouter()


@router.get("/")
async def home():
    return RedirectResponse("/docs", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/players", response_model=list[ChelseaPlayers])
async def players():
    # How many goals did: PLAYER score?
    random_players = db_client.chelsea_players.aggregate([{"$sample": {"size": 3}}])
    return chelsea_players_schema(random_players)
    

@router.get("/nationality")
async def nationality_question():
    # Which player of the followings is from: COUNTRY?
    random_data = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player = chelsea_players_schema(random_data)[0]
    nationality = random_player["nationality"]
    random_players = db_client.chelsea_players.aggregate([{"$match": {"nationality": {"$ne": nationality}}}, 
                                                          {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(random_player)
    return {"nationality": nationality, "corect_answer": random_player["name"], "players": players_array}


@router.get("/position")
async def position_question():
    # Which one of the following players used to play as: POSITION?
    random_data = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player = chelsea_players_schema(random_data)[0]
    position = random_player["position"]
    random_players = db_client.chelsea_players.aggregate([{"$match": {"position": {"$ne": position}}}, 
                                                          {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(random_player)
    return {"position": position, "corect_answer": random_player["name"], "players": players_array}


@router.get("/top_appearances")
async def top_appearances():
    # Which one of these players has the most appearances for chelsea?
    sort_criteria = [("appearances", -1)]
    player_with_most_appearances = chelsea_player_schema(db_client.chelsea_players.find_one(sort=sort_criteria))
    player_with_most_appearances_name = player_with_most_appearances["name"]
    random_players = db_client.chelsea_players.aggregate([
        {"$match": {"name": {"$ne": player_with_most_appearances_name}}}, {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(player_with_most_appearances)
    return {"corect_answer": player_with_most_appearances_name, "players": players_array}


@router.get("/top_goalscorer")
async def top_goalscorer():
    # Which one of these players is the top goalscorer of chelsea?
    sort_criteria = [("goals", -1)]
    player_with_most_goals = chelsea_player_schema(db_client.chelsea_players.find_one(sort=sort_criteria))
    player_with_most_goals_name = player_with_most_goals["name"]
    random_players = db_client.chelsea_players.aggregate([
        {"$match": {"name": {"$ne": player_with_most_goals_name}}}, {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(player_with_most_goals)
    return {"corect_answer": player_with_most_goals_name, "players": players_array}


@router.get("/most_goals")
async def most_goals():
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


@router.get("/most_appearances")
async def most_appearances():
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


# TODO add docstrings
# TODO add content to readme
# TODO start building the frontend that consumes the api
