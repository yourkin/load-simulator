"""
This module contains the main simulator class and CLI entry point.

Classes:
    LoadSimulator: Main class to simulate operations load.
"""

import asyncio
import time
from random import choice, uniform

import typer

from load_simulator.constants import Complexity
from load_simulator.models import LoadConfig, OperationDetailsDict
from load_simulator.operation_executor import OperationExecutor
from load_simulator.utilities import operation_logging

app = typer.Typer()


class LoadSimulator:
    """Main class to simulate a variety of operations."""

    OPERATION_MAP = {
        Complexity.EASY: ["add", "sub"],
        Complexity.MEDIUM: ["mul", "div"],
        Complexity.COMPLICATED: ["exp", "sin"],
    }

    def __init__(self, load_config: LoadConfig):
        """
        Initialize LoadSimulator with the given load configuration.

        Args:
            load_config (LoadConfig): The configuration for this load simulator.
        """
        self.load_config = load_config

    @classmethod
    def default(cls) -> "LoadSimulator":
        """Create a LoadSimulator with default configuration.

        Returns:
            LoadSimulator: A LoadSimulator instance with default configuration.
        """
        return cls(
            LoadConfig(
                seconds_to_run=5,
                complexity=choice(list(Complexity)),
            )
        )

    async def simulate_load(self) -> list[OperationDetailsDict]:
        """Simulate the operations load.

        Returns:
            list[OperationDetailsDict]: A list of operation details.
        """
        operations = []
        end_time = self.load_config.end_time
        rate_limiter = asyncio.Semaphore(self.load_config.max_ops_per_sec)

        while time.time() < end_time:
            async with rate_limiter:
                operation_details = self._execute_random_operation()
                operations.append(operation_details)

        return operations

    def _execute_random_operation(self) -> OperationDetailsDict:
        """Execute a random operation based on the current configuration.

        Returns:
            OperationDetailsDict: The details of the executed operation.
        """
        x = uniform(1, 1e6)
        y = uniform(1, 1e6)
        operation_name = choice(self.OPERATION_MAP[self.load_config.complexity])
        operation_executor = OperationExecutor(x, y)

        with operation_logging(operation_name, x=x, y=y):
            operation_func = getattr(operation_executor, operation_name)
            result = operation_func()

        return OperationDetailsDict(operation=operation_name, x=x, y=y, result=result)


@app.command()
def run_simulator(
        seconds_to_run: int = typer.Option(10, help="Seconds to run the simulation for"),
        complexity: Complexity = typer.Option(
            Complexity.EASY, help="Complexity level for the mathematical operations"
        ),
        max_ops_per_sec: int = typer.Option(
            5, help="Maximum operations to execute per second"
        ),
):
    """Run the LoadSimulator based on the given CLI arguments."""
    load_config = LoadConfig(
        seconds_to_run=seconds_to_run,
        complexity=complexity,
        max_ops_per_sec=max_ops_per_sec,
    )
    simulator = LoadSimulator(load_config)

    asyncio.run(simulator.simulate_load())


if __name__ == "__main__":
    app()
