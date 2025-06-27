import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawl:
        result  = await crawl.arun(
            url = "https://fbref.com/en/comps/9/Premier-League-Stats",
        )
        if result.success:
            print("Crawl successful!")
            print(result.markdown[:300])  # Print first 1000 characters of the markdown

if __name__ == "__main__":
    asyncio.run(main())