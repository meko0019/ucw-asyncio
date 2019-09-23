import asyncio
import datetime
import random
import time


def run_task(task_id, factor):
    start = datetime.datetime.now()
    print(f"Starting task{task_id} at {start.strftime('%H:%M:%S')}")
    # simulate i/o operation using sleep
    time.sleep(random.random()*factor)
    finish = datetime.datetime.now()
    timer = finish - start
    print(f"Task{task_id} completed at {finish.strftime('%H:%M:%S')}, in {timer.total_seconds():.3f} seconds.")

async def coro(task_id, factor):
    start = datetime.datetime.now()
    print(f"Starting task{task_id} at {start.strftime('%H:%M:%S')}")
    # simulate i/o operation using sleep
    await asyncio.sleep(random.random()*factor)
    finish = datetime.datetime.now()
    timer = finish - start
    print(f"Task{task_id} completed at {finish.strftime('%H:%M:%S')}, in {timer.total_seconds():.3f} seconds.")

def run_all_tasks(how_many):
    print("Running tasks sequentially... ")
    start = time.time()
    for i in range(1, how_many + 1):
        run_task(i, 10/how_many)
    print(f"Process took: {time.time() - start : .2f} seconds. \n")

async def main(how_many):
    print("Running tasks concurrently... ")
    start = time.time()
    tasks = [asyncio.create_task(coro(i, 10/how_many)) for i in range(1, how_many + 1)]
    await asyncio.gather(*tasks)
    print(f"Process took: {time.time() - start : .2f} seconds.")


run_all_tasks(100)
asyncio.run(main(100))
