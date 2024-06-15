"""
ISPPJ1 2024
Anonymous Functions

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains an example that shows the dynamic binding of the values to a variable.
"""


def print_the_value_of_i(i: int) -> None:
    print(i)


fs = []

for i in range(5):
    fs.append(lambda: print_the_value_of_i(i))

for f in fs:
    f()
