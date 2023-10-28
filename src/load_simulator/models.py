"""
This module contains Pydantic models used in the Load Simulator application.

Classes:
    OperationDetailsDict: Pydantic model for operation details.
    OperationList: Pydantic model for a list of operations.
    LoadConfig: Pydantic model for load configuration.
"""
import time
import typing as t

from pydantic import BaseModel, Field, field_validator

from load_simulator.constants import (DEFAULT_MAX_OPERATIONS_PER_SECOND,
                                      Complexity)


class OperationDetailsDict(BaseModel):
    """Data model for operation details."""

    operation: str
    x: float
    y: float
    result: t.Any


class OperationList(BaseModel):
    """Data model for list of operations."""

    operations: list[OperationDetailsDict]


class LoadConfig(BaseModel):
    """Data model for simulator configuration."""

    seconds_to_run: int
    complexity: Complexity
    max_ops_per_sec: int = Field(DEFAULT_MAX_OPERATIONS_PER_SECOND)

    @property
    def end_time(self) -> float:
        return time.time() + self.seconds_to_run

    @field_validator("complexity", mode="before")
    def validate_complexity(cls, value: t.Any) -> Complexity:
        """Validator for the 'complexity' field."""
        if isinstance(value, str):
            return Complexity[value.upper()]
        if isinstance(value, Complexity):
            return value
        raise ValueError("Invalid complexity")
