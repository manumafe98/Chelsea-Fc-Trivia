import pandas as pd
import wikipedia as wp
from db.client import db_client
from db.models.model import ChelseaPlayer

html = wp.page("List_of_Chelsea_F.C._players").html().encode("UTF-8")
df = pd.read_html(html, encoding="UTF-8")[1]


for index, row in df.iterrows():
    new_player = ChelseaPlayer(name = str(row["Player"]),
                               nationality = str(row["Nationality"]),
                               position = str(row["Pos"]),
                               career = str(row["Club career"]),
                               appearances = row["Total"],
                               goals = row["Goals"])
    data = new_player.dict()
    db_client.chelsea_players.insert_one(data)
