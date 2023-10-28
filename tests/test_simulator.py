import pytest

from load_simulator.constants import Complexity
from load_simulator.load_simulator import LoadSimulator
from load_simulator.models import LoadConfig


@pytest.mark.asyncio
@pytest.mark.parametrize("complexity", list(Complexity))
async def test_simulator(complexity: Complexity) -> None:
    load_config = LoadConfig(seconds_to_run=2, complexity=complexity, max_ops_per_sec=5)
    simulator = LoadSimulator(load_config)
    try:
        operations = await simulator.simulate_load()
    except (OverflowError, RuntimeError) as e:
        pass
