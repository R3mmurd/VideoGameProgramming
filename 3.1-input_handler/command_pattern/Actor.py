"""
ISPPJ1 2023
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Actor that represents any elements
the actions are executed on.
"""


class Actor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
