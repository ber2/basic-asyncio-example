import time
import pytest
from awaits import individual_task, main


@pytest.mark.asyncio
async def test_individual_task(mocker):
    sleep = mocker.patch("awaits.asyncio.sleep")
    await individual_task(2)
    sleep.assert_awaited_once()

    seconds = sleep.await_args.args[0]
    assert seconds in range(10, 60)


@pytest.mark.asyncio
async def test_main(mocker):
    task = mocker.patch("awaits.individual_task")
    await main(10)
    assert task.await_count == 10
