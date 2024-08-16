"""
ISPPV1 2024
Input handler by commands.

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class JumpAction as specialization of Action.
"""

from Action import Action
from Actor import Actor


class ActionJump(Action):
    def execute(self, target: Actor) -> None:
        print(f"{target} jumps")
