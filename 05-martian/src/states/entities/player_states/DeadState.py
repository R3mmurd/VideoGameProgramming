"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class DeadState for player.
"""

from src.states.entities.BaseEntityState import BaseEntityState


class DeadState(BaseEntityState):
    def enter(self) -> None:
        self.entity.is_dead = True
