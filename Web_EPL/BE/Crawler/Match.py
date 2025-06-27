import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from io import StringIO
import pandas as pd

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


async def crawl_match():
    run_cfg = CrawlerRunConfig(
        css_selector = "div#div_matchlogs_for thead, div#div_matchlogs_for tbody"
    )
    all_data = []
    try:
        async with AsyncWebCrawler() as crawler:
            for team in teams:
                result = await crawler.arun(
                    url = team['url'],
                    config = run_cfg
                )
                df = pd.read_csv(StringIO(result.markdown), sep = '|')
                df.columns = df.columns.str.strip()
                if 'Date' in df.columns:
                    df = df[df['Date'].notna()]
                    df['Date'] = df['Date'].str.strip()
                    df = df[df['Date'] != "Date"] # remove date overlap
                    df = df[df['Date'].str.len() > 0] 
                
                df['Team'] = team['name']
                all_data.append(df)
            data_match = pd.concat(all_data, ignore_index=True)
            data_match.to_csv("match_raw_24_25.csv", index=False)
            print("Crawl match complete")

    except Exception as e:
        print(f"An erorr crawl_match: {e}")

async def main():
    await crawl_match()
if __name__ == "__main__":
    asyncio.run(main())