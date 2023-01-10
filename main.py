import random
import aiohttp
import asyncio
from bs4 import BeautifulSoup

CATEGORIES: list = [
    "https://habr.com/ru/hub/programming/",
    "https://habr.com/ru/hub/python"
]

with open("proxy.txt") as file:
    PROXY_LIST: list = ''.join(file.readline()).split('\n')


async def send_request(url: str, rand_proxy: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=f"http://{rand_proxy}") as resp:
            return await resp.text(encoding="utf-8")


async def parse_category(category_url: list):
    ...


async def main():
    data = [parse_category(category) for category in CATEGORIES]
    await asyncio.gather(*data)


if __name__ == '__main__':
    asyncio.run(main())
