"""
ISPPV1 2023
Anonymous Functions

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that solves the previous problem by creating a closure.
"""
from typing import Callable


def create_print_the_value_of_i(i: int) -> Callable:
    def print_the_value_of_i() -> None:
        print(i)

    return print_the_value_of_i


def create_print_the_value_of_i(i: int) -> Callable:
    return lambda: print(i)


fs = []

for i in range(5):
    fs.append(create_print_the_value_of_i(i))

for f in fs:
    f()
