import time
import pytest
from awaits import individual_task, main


@pytest.mark.asyncio
async def test_individual_task():
    tic = time.time()
    await individual_task(2)
    tac = time.time()

    assert tac - tic >= 10


@pytest.mark.asyncio
async def test_main():
    tic = time.time()
    await main(2)
    tac = time.time()

    assert tac - tic >= 10
