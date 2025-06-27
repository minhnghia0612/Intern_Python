import pandas as pd
from sqlalchemy.orm import Session
from App.database import SessionLocal, engine
from App.models import Team,Rank,Player,Match
from datetime import datetime

session = Session(bind=engine)

df_rank = pd.read_csv('D:/Web_EPL/BE/Data/ranking.csv')

#iterrows: lấy giá trị trong list 'Name': ['Salah', 'Van Dijk'], ->row lấy ra là Salah -> vandijk
for _,row in df_rank.iterrows():
    team = Team(
        name = row['Team'].strip(),
        logo = row['Logo'].strip(),
    )
    session.merge(team)

    rank = Rank(
        rank = int(row['Rk']),
        team_name = row['Team'].strip(),
        matched_played = int(row['MP']),
        win = int(row['W']),
        draw = int(row['D']),
        lose = int(row['L']),
        gd = int(row['GD']),
        points = int(row['Pts']),
    )
    session.add(rank)

df_player = pd.read_csv('D:/Web_EPL/BE/Data/player.csv')

for _,row in df_player.iterrows():
    player = Player(
        player_name = row['Player_name'].strip(),
        player_url = row['Player_url'].strip(),
        nation = row['Nation'].strip() if pd.notnull(row['Nation']) else "",
        pos = row['Pos'].strip(),
        age = int(row['Age']) if str(row['Age']).strip().isdigit() else 0,
        mp = int(row['MP']),
        starts = int(row['Starts']),
        minutes = int(row['Min']),
        team_name = row['Team'].strip(),
    )
    session.add(player)

df_match = pd.read_csv('D:/Web_EPL/BE/Data/match_24_25.csv')

for _,row in df_match.iterrows():
    match = Match(
        date = datetime.strptime(row['Date'].strip(), "%Y-%m-%d"),
        venue = row['Venue'].strip(),
        result = row['Result'].strip(),
        gf = int(row['GF']),
        ga = int(row['GA']),
        opponent = row['Opponent'].strip(),
        team_name = row['Team'].strip(),
    )
    session.add(match)

session.commit()
session.close()   

print("Importing database to succes")

