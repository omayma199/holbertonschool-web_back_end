#!/usr/bin/env python3
"""
Complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create and return a function that multiplies a float by a given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
