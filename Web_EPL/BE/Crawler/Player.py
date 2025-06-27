import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
import pandas as pd
from io import StringIO
import random
import time

teams = [
    {"name": "Liverpool", "url": "https://fbref.com/en/squads/822bd0ba/Liverpool-Stats"},
    {"name": "Arsenal", "url": "https://fbref.com/en/squads/18bb7c10/Arsenal-Stats"},
    {"name": "Manchester City", "url": "https://fbref.com/en/squads/b8fd03ef/2024-2025/Manchester-City-Stats"},
    {"name": "Chelsea", "url": "https://fbref.com/en/squads/cff3d9bb/2024-2025/Chelsea-Stats"},
    {"name": "Newcastle Utd", "url": "https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats"},
    {"name": "Aston Villa", "url": "https://fbref.com/en/squads/8602292d/Aston-Villa-Stats"},
    {"name": "Nott'ham Forest", "url": "https://fbref.com/en/squads/e4a775cb/Nottingham-Forest-Stats"},
    {"name": "Brighton", "url": "https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats"},
    {"name": "Bournemouth", "url": "https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats"},
    {"name": "Brentford", "url": "https://fbref.com/en/squads/cd051869/Brentford-Stats"},
    {"name": "Fulham", "url": "https://fbref.com/en/squads/fd962109/Fulham-Stats"},
    {"name": "Crystal Palace", "url": "https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats"},
    {"name": "Everton", "url": "https://fbref.com/en/squads/d3fd31cc/Everton-Stats"},
    {"name": "West Ham", "url": "https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats"},
    {"name": "Manchester Utd", "url": "https://fbref.com/en/squads/19538871/Manchester-United-Stats"},
    {"name": "Wolves", "url": "https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats"},
    {"name": "Tottenham", "url": "https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats"},
    {"name": "Leicester City", "url": "https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats"},
    {"name": "Ipswich Town", "url": "https://fbref.com/en/squads/b74092de/Ipswich-Town-Stats"},
    {"name": "Southampton", "url": "https://fbref.com/en/squads/33c895d4/Southampton-Stats"},
]

async def crawl_player():
    run_cfg = CrawlerRunConfig(
        css_selector = "div#div_stats_standard_9 thead tr:not([class]),div#div_stats_standard_9 tbody"
    )
    all_data = []
    try:
        async with AsyncWebCrawler(encoding = 'utf-8') as crawler:
            for team in teams:
                result = await crawler.arun(
                    url = team['url'], 
                    config = run_cfg
                )
                df = pd.read_csv(StringIO(result.markdown), sep='|')
                df.columns = df.columns.str.strip()
                #Lọc player khác null && > 0
                if 'Player' in df.columns:
                    df = df[df['Player'].notna()]
                    df['Player'] = df['Player'].str.strip()
                    df = df[df['Player'] != "Player"]
                    df = df[df['Player'].str.len() > 0]
                #Lọc game > 0
                if 'MP' in df.columns:
                    df["MP"] = pd.to_numeric(df["MP"], errors="coerce")
                    df = df[df["MP"] > 0]     
                df['Team'] = team['name']
                all_data.append(df)
            data_player = pd.concat(all_data, ignore_index= True)
            data_player.to_csv("player_raw.csv", index = False)
            print("Crawl player complete")
    except Exception as e:
        print(f"An error {e}")

async def main():
    await crawl_player()

if __name__ == "__main__":
    asyncio.run(main())
