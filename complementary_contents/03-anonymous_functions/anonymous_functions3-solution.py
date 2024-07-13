"""
ISPPJ1 2024
Anonymous Functions

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that solves the previous problem by creating a closure.
"""

from typing import Callable


def create_print_the_value_of_i_1(i: int) -> Callable:
    def print_the_value_of_i() -> None:
        print(i)

    return print_the_value_of_i


def create_print_the_value_of_i_2(i: int) -> Callable:
    return lambda: print(i)


fs1 = []

for i in range(5):
    fs1.append(create_print_the_value_of_i_1(i))

for f in fs1:
    f()

fs2 = []

for i in range(5):
    fs2.append(create_print_the_value_of_i_2(i))

for f in fs2:
    f()
