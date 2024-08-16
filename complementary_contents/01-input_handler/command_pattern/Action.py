"""
ISPPV1 2024
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the interface of an action to be executed
on an target. This interface represents the Command.
"""

from typing import NoReturn

from Actor import Actor


class Action:
    def execute(self, target: Actor) -> NoReturn:
        raise NotImplementedError()
