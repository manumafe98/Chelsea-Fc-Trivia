import pandas as pd
import wikipedia as wp
from db.client import db_client
from db.models.model import ChelseaPlayer

html = wp.page("List_of_Chelsea_F.C._players").html().encode("UTF-8")
df = pd.read_html(html, encoding='UTF-8')[1]


for index, row in df.iterrows():
    new_player = ChelseaPlayer(name = row["Name"],
                               nationality = row["Nationality"],
                               position = row["Position"],
                               career = row["Chelsea career"],
                               appearances = row["Appearances"],
                               goals = row["Goals"])
    data = new_player.dict()
    db_client.chelsea_players.insert_one(data)
