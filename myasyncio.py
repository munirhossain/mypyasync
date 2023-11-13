import time
import asyncio


async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee")
    return "coffee ready"


async def toastBagel():
    print("Start toastBagel()")
    await asyncio.sleep(2)
    print("End toastBagel")
    return "bagel ready"


async def main():
    start_time = time.time()

    # put your operation here
    batch_task = asyncio.gather(brewCoffee(), toastBagel())
    brew_result, toast_result = await batch_task

    # brew_task = asyncio.create_task(brewCoffee())
    # toast_task = asyncio.create_task(toastBagel())
    # brew_result = await brew_task
    # toast_result = await toast_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of brewCoffee: {brew_result}")
    print(f"Result of toastBagel: {toast_result}")
    print(f"Total execution time: {elapsed_time}")

if __name__ == "__main__":
    asyncio.run(main())
