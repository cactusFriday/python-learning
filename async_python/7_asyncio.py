'''
async def - создает корутину с генераторной природой
если просто вызвать такую функцию - получим объект корутины (как объект генератора)
Поэтому вызов корутины предваряется ключевым словом await

'''

import asyncio
# import aiohttp
# python 3.4 -> @asyncio.courutine
# python 3.5 -> async def name() and yield from now is await
# python 3.6 -> ensure_future() -- create_task()
# python 3.7 -> loop creation -- asyncio.run(courutine())


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())
    # task1 = asyncio.create_task(print_nums()) #3.6
    # task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    # asyncio.run(main())       # 3.7