import asyncio


async def some_work(seconds):
    print("DOING SOME WORK.......")
    await asyncio.sleep(seconds)
    print("WORD DONE.")


async def main():
    task1 = asyncio.create_task(some_work(2))
    task2 = asyncio.create_task(some_work(5))
    print("HELLLO....")
    await task1
    print("...WORLD")
    await task2

asyncio.run(main())