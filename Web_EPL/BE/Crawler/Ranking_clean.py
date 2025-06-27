import pandas as pd
import re

def extract_team_and_logo(x: str):
    pattern = r'!\[.*?\]\((.*?)\) \[(.*?)\]\(.*?\)' #dùng để tách []() []()
    matches = re.findall(pattern, x)
    team = ""
    logo = ""

    if matches:
        logo = matches[0][0]
        team = matches[0][1]
    return logo,team

def clean_ranking():
    try:
        df = pd.read_csv("ranking_raw.csv")
        df.columns = df.columns.str.strip()
        df[['Logo', 'Team']] = df['Squad'].apply(
            lambda x: pd.Series(extract_team_and_logo(x))
        )
        df = df[["Rk","Logo", "Team", "MP", "W", "D", "L", "GD", "Pts"]]
        df.to_csv("D:/Web_EPL/Data/ranking.csv", index=False)
        print("Cleaned ranking data saved successfully.")
    except Exception as e:
        print(f"An error occurred while cleaning the ranking data: {e}")

def main():
    clean_ranking()
if __name__ == "__main__":
    main()