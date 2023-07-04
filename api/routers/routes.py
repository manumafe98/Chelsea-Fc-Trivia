from fastapi import APIRouter
from db.client import db_client
from db.models.model import ChelseaPlayers
from db.schemas.schemas import chelsea_players_schema, chelsea_player_schema


router = APIRouter()

@router.get("/players", response_model=list[ChelseaPlayers])
async def players():
    random_players = db_client.chelsea_players.aggregate([{"$sample": {"size": 3}}])
    return chelsea_players_schema(random_players)
    

@router.get("/nationality", response_model=list[ChelseaPlayers])
async def nationality_question():
    random_data = db_client.chelsea_players.aggregate([{"$sample": {"size": 1}}])
    random_player = chelsea_players_schema(random_data)[0]
    nationality = random_player["nationality"]
    random_players = db_client.chelsea_players.aggregate([{"$match": {"nationality": {"$ne": nationality}}}, 
                                                          {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(random_player)
    return players_array


@router.get("/top_appearances", response_model=list[ChelseaPlayers])
async def top_appearances():
    sort_criteria = [("appearances", -1)]
    player_with_most_appearances = chelsea_player_schema(db_client.chelsea_players.find_one(sort=sort_criteria))
    player_with_most_appearances_name = player_with_most_appearances["name"]
    random_players = db_client.chelsea_players.aggregate([
        {"$match": {"name": {"$ne": player_with_most_appearances_name}}}, {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(player_with_most_appearances)
    return players_array


@router.get("/top_goalscorer", response_model=list[ChelseaPlayers])
async def top_goalscorer():
    sort_criteria = [("goals", -1)]
    player_with_most_goals = chelsea_player_schema(db_client.chelsea_players.find_one(sort=sort_criteria))
    player_with_most_goals_name = player_with_most_goals["name"]
    random_players = db_client.chelsea_players.aggregate([
        {"$match": {"name": {"$ne": player_with_most_goals_name}}}, {"$sample": {"size": 2}}])
    players_array = chelsea_players_schema(random_players)
    players_array.append(player_with_most_goals)
    return players_array


# Example questions:
# Which player of the following have the most goals?
# Which player of the following have the most appereances?
# Which player of the followings is from: COUNTRY?
# Which one of the following players used to play as: POSITION?
# Which one of the following players played for chelsea in this frame of time: CAREER?

# Podriamos hacer a la inversa, tambien tipo seleccionar el nobmre del jugador y poner 3 respuestas con numeros de goles
# y viceversa
# How many goals did: PLAYER score?