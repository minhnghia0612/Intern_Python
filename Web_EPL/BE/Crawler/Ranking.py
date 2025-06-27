import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from io import StringIO
import pandas as pd
async def crawl_ranking():
    run_cfg = CrawlerRunConfig(
        css_selector="div#div_results2024-202591_overall thead,div#div_results2024-202591_overall tbody",   # crawl theo theo id
    )
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url = "https://fbref.com/en/comps/9/Premier-League-Stats",
                config = run_cfg
            )
        cleaned = result.markdown.replace('"', '') # Xoa dau ngoac kep

        df = pd.read_csv(StringIO(cleaned), sep='|')  # Doc du lieu tu chuoi StringIO
        df.to_csv("ranking_raw.csv", index = False)  # Luu du lieu vao file csv

        print("Crawl rank complete")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Crawl failed")
async def main():
    await crawl_ranking()

if __name__ == "__main__":
    asyncio.run(main())
