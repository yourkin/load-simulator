"""
Utilities
=========
This module contains utility functions and context managers used in the Load Simulator application.

Functions:
    operation_logging: Context manager for logging operations.
"""

import logging
import typing as t
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)


@contextmanager
def operation_logging(operation_name: str, **kwargs: t.Any):
    """Context manager for logging operations."""
    logging.info(f"Operation {operation_name} started with parameters: {kwargs}")
    yield
    logging.info(f"Operation {operation_name} completed")
