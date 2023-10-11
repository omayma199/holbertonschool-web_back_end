#!/usr/bin/env python3
"""
Measure the runtime
"""
from time import time
from wait_n import wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the runtime
    """
    start_time = time()
    
    # Measure the total execution time for wait_n(n, max_delay)
    wait_n(n, max_delay)
    
    end_time = time()
    
    # Calculate the total time and return the average time per iteration
    total_time = end_time - start_time
    average_time_per_iteration = total_time / n
    return average_time_per_iteration
