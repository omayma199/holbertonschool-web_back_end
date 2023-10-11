#!/usr/bin/env python3
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string and an int/float to a tuple with the string and the square of the int/float as a float."""
    squared_value = float(v) ** 2
    return k, squared_value
