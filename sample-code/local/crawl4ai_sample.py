import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://en.wikipedia.org/wiki/OpenAI",
        )
        print(result.markdown)
        print(result.pdf)

if __name__ == "__main__":
    asyncio.run(main())