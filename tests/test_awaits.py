import time
import pytest
from unittest import mock
from awaits import individual_task, main


@pytest.mark.asyncio
@mock.patch("awaits.asyncio.sleep")
async def test_individual_task(sleep):
    await individual_task(2)
    sleep.assert_awaited_once()

    seconds = sleep.await_args.args[0]
    assert seconds in range(10, 60)


@pytest.mark.asyncio
@mock.patch("awaits.asyncio.sleep")
async def test_main(sleep):
    await main(10)
    assert sleep.await_count == 10
    times = [call.args[0] for call in sleep.await_args_list]
    assert all(time in range(10, 60) for time in times)
