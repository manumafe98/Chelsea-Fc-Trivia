import pandas as pd
import wikipedia as wp
from db.client import db_client
from db.models.model import ChelseaPlayer

html = wp.page("List_of_Chelsea_F.C._players").html().encode("UTF-8")
df = pd.read_html(html, encoding="UTF-8")[1]

for index, row in df.iterrows():

    new_player = ChelseaPlayer(name = row.iloc[0],
                               nationality = row.iloc[1],
                               position = row.iloc[2],
                               career = row.iloc[3],
                               appearances = row.iloc[4],
                               goals = row.iloc[5])
    data = new_player.dict()
    db_client.chelsea_players.insert_one(data)
