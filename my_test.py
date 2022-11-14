# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import re
import asyncio


async def fun1():
    print('START')
    await asyncio.sleep(2)
    print('END')


async def fun2():
    print('START NEW')
    await asyncio.sleep(2)
    print('END NEW')


def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(fun1())
    task2 = loop.create_task(fun2())
    loop.run_until_complete(asyncio.wait([task1, task2]))


if __name__ == '__main__':
    main()
