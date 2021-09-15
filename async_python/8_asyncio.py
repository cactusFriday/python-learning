import asyncio
import aiohttp
from time import time
import requests


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r

def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(response.content)

def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)




############################## ASYNC ##############################

def write_image(data):
    filename = f'file-{(int(time() * 1000))}.jpg'
    with open(filename, 'wb') as file:
        file.write(data)


# Первая корутина, которая принимает сессию и работает с ней через асинхронный менеджер, 
# в последствии, т.к. response объект генератор (асинхронный) - используем await
async def fetch_content(url, session):
    async with session.get(url, allow_redirects = True) as response:
        data = await response.read()
        write_image(data)

async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.ensure_future(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)




if __name__ == '__main__':
    t0 = time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main2())
    loop.close()
    print(time() - t0)