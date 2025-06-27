import pandas as pd
import re
from Player_clean import extract

def clean_match():
    try:
        df = pd.read_csv("match_raw_24_25.csv")
        df.columns = df.columns.str.strip()
        df[['Date', 'Url']] = df['Date'].apply(
            lambda x: pd.Series(extract(x))
        )
        df[['Opponent', 'Url']] = df['Opponent'].apply(
            lambda x: pd.Series(extract(x))
        )
        df = df[df['GA'].str.len() == 2]
        df = df[df['GF'].str.len() == 2] 
        df = df[['Date', 'Venue', 'Result', 'GF', 'GA', 'Opponent', 'Team']]
        df.to_csv("D:/Web_EPL/Data/match_24_25.csv", index=False)
        print("clean match 24-25 complete")
    except Exception as e:
        print(f"Clean ranking erorr:{e}")

def main():
    clean_match()
if __name__ == "__main__":
    main()