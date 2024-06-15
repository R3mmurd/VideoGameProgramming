"""
ISPPJ1 2024
Anonymous Functions

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example of a function that returns an anonymous function.
"""

from typing import Callable


def build_power_function(x: float, y: float) -> Callable:
    return lambda: x**y


def build_power_three_function() -> Callable:
    return lambda x: x**3


power2_3 = build_power_function(2, 3)
print(power2_3())

power2_4 = build_power_function(2, 4)
print(power2_4())

power_3 = build_power_three_function()
print(po)
