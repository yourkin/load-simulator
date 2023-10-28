"""
This module contains constants and enumerations used in the Load Simulator application.

Classes:
    Complexity: Enum to represent operation complexity.
"""
from enum import Enum, auto

# Rate Limiting
DEFAULT_MAX_OPERATIONS_PER_SECOND = int(1e6)


class Complexity(Enum):
    """Enumeration for different types of operation complexities."""

    EASY = "easy"
    MEDIUM = "medium"
    COMPLICATED = "complicated"
