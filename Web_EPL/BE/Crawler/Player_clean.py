import pandas as pd
import re

def extract(x: str):
    pattern = r'\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, x)
    name = ""
    url = ""
    if matches:
        name = matches[0][0]
        url = matches[0][1]
    return name,url


def clean_player():
    try:
        df = pd.read_csv("player_raw.csv", quotechar='"' ,thousands=',')
        df.columns = df.columns.str.strip()
        df[['Player_name', 'Player_url']] = df['Player'].apply(
            lambda x: pd.Series(extract(x))
        )
        df[['Nation','Nation_url']] = df['Nation'].apply(
            lambda x: pd.Series(extract(x))
        )
        df['Nation'] = df['Nation'].str[-3:]
        df['Min'] = df['Min'].astype(str).str.strip(' "')
        df['Pos'] = df['Pos'].astype(str).str.strip()
        df = df[['Player_name', 'Player_url', 'Nation', 'Pos', 'Age', 'MP', 'Starts', 'Min', 'Team']]
        df.to_csv("D:/Web_EPL/Data/player.csv", index=False)
        print("Clean player complete")
    except Exception as e:
        print(f"An error clean player data: {e}")

def main():
    clean_player()
if __name__ == "__main__":
    main()       