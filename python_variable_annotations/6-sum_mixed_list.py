#!/usr/bin/env python3
"""
sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sum of a mixed list of integers and floats and return float."""
    return float(sum(mxd_lst))
