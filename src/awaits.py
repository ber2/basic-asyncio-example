import asyncio
import random


async def individual_task(task_number: int) -> None:
    seconds = random.randrange(10, 60)
    print(f"{task_number}\t{seconds}")
    await asyncio.sleep(seconds)
    print(f"Task {task_number} done")


async def main(n_tasks: int) -> None:

    print("Task #\tTime")
    print("-------------")

    tasks = [asyncio.create_task(individual_task(d)) for d in range(1, n_tasks + 1)]
    for task in tasks:
        await task


if __name__ == "__main__":
    asyncio.run(main(20))
