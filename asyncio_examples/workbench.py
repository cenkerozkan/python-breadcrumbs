import asyncio

async def sleep_method():
    print("Entering sleep method")
    await asyncio.sleep(15)
    print("Exiting sleep method")

async def sleep_method2():
    print("Entering sleep method2")
    await asyncio.sleep(10)
    print("Exiting sleep method2")

async def main():
    task_list = [sleep_method(), sleep_method2()]
    await asyncio.gather(*task_list)

# Run the async program
asyncio.run(main())