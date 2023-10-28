"""
This module contains the class responsible for executing mathematical operations.

Classes:
    OperationExecutor: Executor class to carry out mathematical operations.
"""
import math
import typing as t
from dataclasses import dataclass


class OperationExecutorMeta(type):
    """MetaClass to dynamically generate OperationExecutor methods."""

    def __new__(cls, name: str, bases: t.Any, class_dict: dict) -> t.Any:
        operations = {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "mul": lambda x, y: x * y,
            "div": lambda x, y: x / y,
            "exp": lambda x: math.exp(x),
            "sin": lambda x: math.sin(x),
        }
        for operation_name, operation_func in operations.items():

            def method(self: t.Any, operation_func=operation_func) -> t.Any:
                return (
                    operation_func(self.x, self.y)
                    if operation_func.__code__.co_argcount == 2
                    else operation_func(self.x)
                )

            class_dict[operation_name] = method
        return super().__new__(cls, name, bases, class_dict)


@dataclass
class OperationExecutor(metaclass=OperationExecutorMeta):
    """Executor class for mathematical operations."""

    x: float
    y: float
