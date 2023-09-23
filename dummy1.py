import aiohttp
import asyncio

async def fetch_random_wikipedia_url(session, url):
    timeout = aiohttp.ClientTimeout(total=30000)  # Increase the timeout to 30 seconds
    async with session.get(url, timeout=timeout) as response:
        if response.status == 200:
            random_url = str(response.url)
            article_keyword = random_url.split("https://en.wikipedia.org/wiki/", 1)[1]
            # print(f"Fetched URL {count}: {article_keyword}")
            return article_keyword
        return None

async def main():
    SAMPLE_SIZE = 100
    base_url = "https://en.wikipedia.org/wiki/Special:Random"

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_random_wikipedia_url(session, base_url) for _ in range(SAMPLE_SIZE)]
        results = await asyncio.gather(*tasks)

    with open("./articles.txt", "w+") as f:
        for result in results:
            if result:
                f.write(result + "\n")

if __name__ == "__main__":
    asyncio.run(main())











# import requests
# SAMPLE_SIZE = 5000

# f = open("./articles.txt", "w+")

# for _ in range(SAMPLE_SIZE):
#     response = requests.get("https://en.wikipedia.org/wiki/Special:Random")
#     random_url = response.url
#     atrticleKeyword = random_url.split("https://en.wikipedia.org/wiki/", 1)[1]
#     f.write(atrticleKeyword+"\n")
